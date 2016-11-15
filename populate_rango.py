import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # Primero creamos listas de diccionarios que contengan las paginas que queremos agregar a cada categoria
    # Luego, creamos un diccionario de diccionarios para nuestras categorias
    # Esto puede ser confuso, pero nos permite iterar cada estructura de datos y agregar los datos a nuestros modelos

    python_pages = [
        {"title": "Official Python Tutorial",
            "url": "http://docs.python.org/2/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
            "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
            "url": "http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
            "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks",
            "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
            "url": "http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title": "Bottle",
            "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
            "url": "http://flask.pocoo.org"}
    ]

    cats = {
        "Python": {"pages": python_pages},
        "Django": {"pages": django_pages},
        "Other Frameworks": {"pages": other_pages}
    }

    # El codigo debajo recorre el diccionario 'cats', luego agrega cada categoria,
    # luego agrega todas las paginas asociadas en cada categoria

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    # Imprimimos las categorias que hemos agregado
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
