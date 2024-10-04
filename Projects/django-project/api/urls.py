from django.conf.urls import include
from django.urls import path

from api.views import ProductView, ProductsView


urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    # Product
    path(
        name="get_products",
        route="products/",
        view=ProductsView.as_view()
    ),
    path(
        name="get_product",
        route="products/<int:product_id>",
        view=ProductView.as_view()
    )
]
