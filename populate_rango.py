import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'tango_with_django_project.settings')
from random import randint

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/'} 
        ]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/'}
    ]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask',
        'url':'http://flask.pocoo.org'} 
        ]

    cats = {'Python': {'pages': python_pages}, 
        'Django': {'pages': django_pages},
        'Other Frameworks': {'pages': other_pages} }


    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    if (p.views == 0):
        p.views = randint(1,101)
    p.save()
    return p

cat_views_likes = {
    'Python': {'views': 128, 'likes': 64},
    'Django': {'views': 64, 'likes': 32},
    'Other Frameworks': {'views': 32, 'likes': 16, } }

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = cat_views_likes[c.name]['views']
    c.likes = cat_views_likes[c.name]['likes']
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
