from django.urls import path

from route import views

app_name = "route"

urlpatterns = [
    path("<slug:route_slug>/", views.route_index, name="route_index"),
    path("<slug:route_slug>/route_descr/", views.route_descr, name="route_descr"),
    path("<slug:route_slug>/route_city/", views.route_city, name="route_city"),
]
