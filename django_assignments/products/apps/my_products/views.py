# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product


def index(request):
    product = Product.objects.create(name="Noel", description="Hello World",
                                     weight=10, price=700, cost=700, category="none")
    products = Product.objects.all()
    # name = product.name
    print product.name
    new_product = product.name, product.description, product.weight, product.price, product.cost, product.category
    for new in new_product:
        print new
    context = {
        'product': new
    }
    print product
    return render(request, "my_products/index.html", context)
