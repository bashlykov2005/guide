from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def route_index(request):
    context = {
        "title": "Маршрут",
    }
    return render(request, "route/route.html", context)


def route_descr(request):
    context = {
        "title": "Описание маршрута",
    }
    return render(request, "route/route-description.html", context)


def route_city(request):
    context = {
        "title": "Базовый город",
    }
    return render(request, "route/route-base-city.html", context)
