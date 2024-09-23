from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Информация",
    }
    return render(request, "main/about.html", context)
