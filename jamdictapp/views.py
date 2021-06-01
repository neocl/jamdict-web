# -*- coding: utf-8 -*-

"""
Jamdict web - Japanese Reading Assistant
"""

# This code is a part of jamdict-web library: https://github.com/neocl/jamdict-web
# :copyright: (c) 2021 Le Tuan Anh <tuananh.ke@gmail.com>
# :license: MIT, see LICENSE for more details.

import json
import re
import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from chirptext import __version__ as chirptext_version
from chirptext import deko
from speach import ttlig as tig
from jamdict import Jamdict
from jamdict import __version__ as jamdict_version
import jaconv

from .util import JAMDICT_POS_MAP


def logger():
    return logging.getLogger(__name__)


jam = Jamdict(reuse_ctx=False)


def jsonp(func):
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        data = json.dumps(objects)
        if 'callback' in request.GET:
            callback = request.GET['callback']
        elif 'callback' in request.POST:
            callback = request.POST['callback']
        else:
            return HttpResponse(data, "application/json")
        data = '{c}({d});'.format(c=callback, d=data)
        return HttpResponse(data, "application/javascript")
    return decorator


def index(request):
    return render(request, "jamdictapp/index.html")


# ------------------------------------------------------------------------------
# Parsing
# ------------------------------------------------------------------------------

FORCE_NEWLINE = re.compile(r"。([^\n])")


def tokenize(text):
    with_newline = FORCE_NEWLINE.sub(lambda x: '。\n' + x.group(1), text)
    return [x.replace('\n','').replace('\r', '') for x in re.split('\n{2,}', with_newline) if x.strip()]


@jsonp
@csrf_protect
def parse_doc(request, text=''):
    if request.method == "POST":
        text = request.POST.get('text', '')
    sents = []
    for chunk in tokenize(text):
        for txt in chunk.splitlines():
            sent = deko.parse(txt)
            sent_dict = sent.to_dict()
            for tk_dict, tk in zip(sent_dict['tokens'], sent):
                r = tig.RubyToken.from_furi(tk.text, tk.reading_hira)
                if r.to_code() != tk.text:
                    tk_dict['furi'] = r.to_html()
                tk_dict['romaji'] = jaconv.kana2alphabet(tk.reading_hira)
            sents.append(sent_dict)
    return {'sents': sents}


@jsonp
@csrf_protect
def version(request):
    return {"chirptext": chirptext_version,
            "jamdict": jamdict_version}


# ---------------------------------------------------------------------
# Jamdol
# ---------------------------------------------------------------------

@jsonp
@csrf_protect
def jamdict_search(request, query=None, strict=None):
    if request.method == "POST":
        query = request.POST.get('query', '')
        strict = request.POST.get('strict', '') == 'true'
    results = jam.lookup(query, strict_lookup=strict)
    # if found nothing, may be input = romaji?
    if not results.entries and not results.chars and not results.names:
        query = jaconv.alphabet2kana(query)
        results = jam.lookup(query, strict_lookup=strict)
    # try kata also
    if not results.entries and not results.chars and not results.names:
        query = jaconv.alphabet2kata(query)
        results = jam.lookup(query, strict_lookup=strict)
    result_dict = results.to_dict()
    # simplify POS
    for entry in result_dict['entries']:
        for sense in entry['senses']:
            if 'pos' in sense:
                for idx in range(len(sense['pos'])):
                    pos = sense['pos'][idx]
                    if pos in JAMDICT_POS_MAP:
                        sense['pos'][idx] = {'text': JAMDICT_POS_MAP[pos].upper(),
                                             'desc': pos}
    return result_dict
