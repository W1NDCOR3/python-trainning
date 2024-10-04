from django.db import models


class Client(models.Model):
    name = models.CharField(
        blank=False,
        max_length=256,
        primary_key=False,
        unique=False,
        null=False,
        verbose_name="Name",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        blank=False,
        max_length=256,
        primary_key=False,
        unique=False,
        null=False,
        verbose_name="Name",
    )
    price = models.FloatField(
        blank=False,
        primary_key=False,
        unique=False,
        null=False,
        verbose_name="Price",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        max_length=256,
        primary_key=False,
        unique=False,
        related_name="client_cart",
        verbose_name="Client",
    )
    products = models.ManyToManyField(
        Product,
        blank=True,
        primary_key=False,
        unique=False,
        related_name="products_cart",
        verbose_name="Products",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def name(self):
        return f"{self.client.name}'s cart" if self.client else "Ghost cart"