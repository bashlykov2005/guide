from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

from route.models import Route
from country.models import Сountry
from brewery.models import Brewery


def index(request):

    routes = Route.objects.all()
    route_dark = range(1, 5)
    route_light = range(5, 50)
    route_disabled = range(50, 100)

    context = {
        "title": "Главная",
        "routes": routes,
        "route_dark": route_dark,
        "route_light": route_light,
        "route_disabled": route_disabled,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Информация",
    }
    return render(request, "main/about.html", context)
