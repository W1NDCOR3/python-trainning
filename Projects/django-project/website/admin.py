from django.contrib import admin

from website.models import Cart, Client, Product


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created",
        "updated",
    )
    list_display_links = ("name",)


admin.site.register(Client, ClientAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created",
        "updated",
    )
    list_display_links = ("name",)


admin.site.register(Cart, CartAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created",
        "updated",
    )
    list_display_links = ("name",)


admin.site.register(Product, ProductAdmin)
