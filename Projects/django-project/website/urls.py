from django.urls import path
from website.views import ClientView, HomeView, add_product, remove_product


urlpatterns = [
    # Home
    path(
        name="home",
        route="",  # localhost:8000/website/
        view=HomeView.as_view(),
    ),
    # Client
    path(
        name="client",
        route="client/<int:client_id>",  # localhost:8000/website/client/1
        view=ClientView.as_view(),
    ),
    # Product
    path(
        name="add_product",
        # localhost:8000/website/client/1/cart/1/product/1
        route="client/<int:client_id>/cart/<int:cart_id>/product/<int:product_id>",
        view=add_product,
    ),
    path(
        name="remove_product",
        # localhost:8000/website/client/1/cart/1/product/1
        route="client/<int:client_id>/cart/<int:cart_id>/product/<int:product_id>/remove",
        view=remove_product,
    ),
]
