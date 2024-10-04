from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.views import View

from website.models import Cart, Client, Product


class HomeView(View):
    def get(self, request: HttpRequest):
        clients = Client.objects.all()

        return render(
            request=request,
            template_name="home.html",
            context={
                "clients": clients,
            },
        )


def add_product(_: HttpRequest, client_id: int, product_id: int, cart_id: int):
    cart = Cart.objects.filter(id=cart_id).first()

    if not cart:
        return redirect("home")

    product = Product.objects.filter(id=product_id).first()

    if not product:
        return redirect("home")

    product_exists = product in cart.products.all()

    if product_exists:
        return redirect("home")

    cart.products.add(product)
    cart.save()

    return redirect("client", client_id=client_id)


def remove_product(_: HttpRequest, client_id: int, product_id: int, cart_id: int):
    cart = Cart.objects.filter(id=cart_id).first()
        
    if not cart:
        return redirect("home")

    product = cart.products.filter(id=product_id).first()

    if not product:
        return redirect("home")

    cart.products.remove(product)
    cart.save()

    return redirect("client", client_id=client_id)


class ClientView(View):
    def get(self, request: HttpRequest, client_id: int):
        client = Client.objects.filter(id=client_id).first()

        if not client:
            return redirect("home")

        cart_objects = Cart.objects.filter(client=client_id)

        carts = []
        for cart_object in cart_objects:
            all_products = Product.objects.all()
            products = cart_object.products.all()
            missing_products = set(all_products) - set(products)

            carts.append(
                {
                    "id": cart_object.id,  # type: ignore
                    "products": products,
                    "missing_products": missing_products,
                }
            )

        return render(
            request=request,
            template_name="client.html",
            context={
                "client_id": client_id,
                "carts": carts,
            },
        )
