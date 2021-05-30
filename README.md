# jamdict-web
Japanese Reading Assistant with morphological analyser, Japanese-English dictionary, Kanji dictionary, and Japanese Names dictionary

## Online demo

There is a demo instance of Jamdict-web - Japanese Reading Assistant online if you just want to try it out:

https://jamdict.herokuapp.com/

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

Jamdict-web was developed based on the following products:

- 
