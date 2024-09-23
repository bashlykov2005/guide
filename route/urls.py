from django.urls import path

from route import views

app_name = "route"

urlpatterns = [
    path("", views.route_index, name="route_index"),
    path("route_descr/", views.route_descr, name="route_descr"),
    path("route_city/", views.route_city, name="route_city"),
]
