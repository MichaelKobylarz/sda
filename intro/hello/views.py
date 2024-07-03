import datetime
from typing import Dict
from django.shortcuts import render, HttpResponse

from hello.utils import Cow


# Create your views here.
def hello_view(request):
    return HttpResponse("Witaj świecie!")


def hi_view(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
            <h2>Hello, world!</h2>
        </body>
    </html>
    """)


# szablon
def hi2_view(request):
    return render(request, 'hello.html')


def jurek_view(request):
    return HttpResponse("Witaj, Jurek!")


def jacek_view(request):
    return HttpResponse("Witaj, Jacek!")


def ksawier_view(request):
    return HttpResponse("Witaj, Ksawier!")


# Podatność XSS - przykład
def name_view(request, name):
    # importy powinny być zawsze na samej górze
    from django.utils.html import escape

    # always remember to escape your output
    print(name)
    escaped_name = escape(name)
    print(escaped_name)

    return HttpResponse(f"Witaj, {name}!")


# kontekst szablonu
def name_view2(request, name):
    return render(
        request,
        'hello2.html',
        {"name": name}
    )


def is_it_new_year(request):

    today = datetime.date.today()

    is_new_year = False
    if today.month == 1 and today.day == 1:
        is_new_year = True

    return render(
        request,
        'isitnewyear.html',
        {'is_new_year': is_new_year}
    )


def collection_view(request):

    fruits = [
        'jabłko',
        'banan',
        'winogrona',
        'mandarynki'
    ]

    person = {
        "name": "Jan",
        "surename": "Kowalski",
        "age": 25
    }

    cow = Cow("Mućka", 3)

    return render(
        request,
        'collection.html',
        {
            'fruits': fruits,
            'person': person,
            'cow': cow
        }
    )

