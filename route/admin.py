from django.contrib import admin

from route.models import Route

class RouteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "base_city",
        "city_desc",
        "route_desc",
        "link",
        "image_route1",
        "image_route2",
        "image_route3",
        "image_route4",
        "image_route5",
        "image_route6",
        "image_city1",
        "image_city2",
        "image_city3",
        "image_city4",
    )
    list_display_links = ('id',)
    search_fields = ("name", 'base_city')
    list_editable = (
        "name",
        "slug",
        "base_city",
        "city_desc",
        "route_desc",
        "link",
        "image_route1",
        "image_route2",
        "image_route3",
        "image_route4",
        "image_route5",
        "image_route6",
        "image_city1",
        "image_city2",
        "image_city3",
        "image_city4",
    )
    list_filter = ("name", "base_city",)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Route, RouteAdmin)
