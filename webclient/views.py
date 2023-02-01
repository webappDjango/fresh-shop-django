from django.shortcuts import render
from django.http import HttpRequest
from product import models

# Create your views here.
def index(request: HttpRequest):
    return render(request, "webclient/index.html")

def shop(request: HttpRequest):
    products = models.Product.objects.all()
    return render(request, "webclient/shop.html", {"products": products})

def about(request: HttpRequest):
    return render(request, "webclient/about.html")

def cart(request: HttpRequest):
    return render(request, "webclient/cart.html")

def checkout(request: HttpRequest):
    return render(request, "webclient/checkout.html")

def contact_us(request: HttpRequest):
    return render(request, "webclient/contact-us.html")

def gallery(request: HttpRequest):
    return render(request, "webclient/gallery.html")

def my_account(request: HttpRequest):
    return render(request, "webclient/my-account.html")

def shop_detail(request: HttpRequest):
    return render(request, "webclient/shop-detail.html")

def wishlist(request: HttpRequest):
    return render(request, "webclient/wishlist.html")