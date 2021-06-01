# jamdict-web

**Japanese Reading Assistant** with morphological analyser, Japanese-English dictionary, Kanji dictionary, and Japanese Names dictionary

## Online demo

There is a demo instance of Jamdict-web - Japanese Reading Assistant online if you just want to try it out:

https://jamdict.herokuapp.com/

![Jamdict-web screenshot](https://raw.githubusercontent.com/wiki/neocl/jamdict-web/images/jamdict-screenshot.png)

## Local development

You can run this software locally on your computer like this

```bash
git clone https://github.com/neocl/jamdict-web
cd jamdict-web

# create a Python virtual environment
mkvirtualenv jamdict-web

pip install -r requirements.txt

python manage.py collectstatic
python manage.py migrate
python manage.py runserver
```

## Credit

**Jamdict-web / Japanese Reading Assistant** was developed by [Le Tuan Anh](https://github.com/letuananh) and released under MIT License.

The following products were used in the development:

[Jamdict](https://github.com/neocl/jamdict): Japanese dictionary package for Python 3 (MIT License)

[JMDict](https://www.edrdg.org/wiki/index.php/Main_Page#The_JMdict.2FEDICT_Project): a freely-usable general Japanese electronic dictionary [(CC BY-SA 3.0 License)](https://www.edrdg.org/edrdg/licence.html)

[JMnedict](https://www.edrdg.org/wiki/index.php/Main_Page#The_ENAMDICT.2FJMnedict_Project): 740,000 Japanese proper names (place, people, company, product, etc.) [(CC BY-SA 3.0 License)](https://www.edrdg.org/edrdg/licence.html)

[KANJIDIC](http://www.edrdg.org/wiki/index.php/Main_Page#The_KANJIDIC_Project): a comprehensive kanji database [(CC BY-SA 3.0 license)](https://www.edrdg.org/edrdg/licence.html)

[Igo-python](https://pypi.org/project/igo-python/): a Python port of Igo Japanese morphological analyzer (MIT License)

[Kanji Stroke Order](https://www.nihilist.org.uk): Japanese font with writing stroke order (Version 4.004) [(BSD License)](https://www.nihilist.org.uk)

[jaconv](https://pypi.org/project/jaconv/): interconverter for Hiragana, Katakana, Hankaku (half-width character) and Zenkaku (full-width character) (MIT License)

[Bootstrap 4.6](https://getbootstrap.com/docs/4.6): Free and open-source CSS framework (MIT License)

[Vue.js](https://vuejs.org): open-source front end JavaScript framework (MIT License)

[Sample text](https://www.aozora.gr.jp/cards/000148/files/799_14972.html): from「夢十夜」by 夏目漱石

