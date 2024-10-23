from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

from route.models import Route


def route_index(request, route_slug):

    route = Route.objects.get(slug=route_slug)

    context = {
        "title": "Маршрут",
        'route': route,
    }
    return render(request, "route/route.html", context=context)


def route_descr(request, route_slug):

    route = Route.objects.get(slug=route_slug)

    context = {
        "title": "Описание маршрута",
        "route": route,
    }
    return render(request, "route/route-description.html", context=context)


def route_city(request, route_slug):

    route = Route.objects.get(slug=route_slug)

    context = {
        "title": "Базовый город",
        "route": route,
    }
    return render(request, "route/route-base-city.html", context=context)
