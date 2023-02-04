from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from product import models as productModels
from webclient import models

def _CheckAccessing(request: HttpRequest):
    if "UserId" in request.POST:
        return request.POST["UserId"]
    else:
        return None

# Create your views here.
# chức năng khách
def index(request: HttpRequest):
    return render(request, "webclient/index.html")

def contact_us(request: HttpRequest):
    return render(request, "webclient/contact-us.html")

def shop(request: HttpRequest):
    productsPerPage = 12

    if "page" in request.GET:
        page = request.GET["page"]
    else:
        page = 1
    
    if productModels.Product.objects.count() > (page-1)*productsPerPage:
        begin = (page-1)*productsPerPage
        if productModels.Product.objects.count() > (page * productsPerPage):
            end = page * productsPerPage
        else:
            end = productModels.Product.objects.count()
    else:
        begin = 0
        end = productsPerPage

    products = productModels.Product.objects.all().order_by("id")[begin: end]
    return render(request, "webclient/shop.html", {"products": products})

def about(request: HttpRequest):
    return render(request, "webclient/about.html")

#chức năng người dùng
def cart(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("sign_in?error=Sign in first")
    return render(request, "webclient/cart.html")

def checkout(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("sign_in?error=Sign in first")
    return render(request, "webclient/checkout.html")

def my_account(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("sign_in?error=Sign in first")
    return render(request, "webclient/my-account.html")

def wishlist(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("sign_in?error=Sign in first")
    return render(request, "webclient/wishlist.html")

#đăng ký và đăng nhập
def sign_up(request: HttpRequest):
    if "username" in request.POST:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        phone = request.POST["phone"]

        result = models.User.Sign_up(username, email, password,repassword, phone)
        if result == "Successfully":
            return HttpResponseRedirect("sign_in")
        else:
            return render(request, "webclient/sign-up.html", {"error": result})
    return render(request, "webclient/sign-up.html")

def sign_in(request: HttpRequest):
    if "email" in request.POST:
        email = request.POST["email"]
        password = request.POST["password"]

        result = models.User.CheckLogin(email, password)
        if result is models.User:
            request.session['UserId'] = result.id
            return HttpResponseRedirect("index")
        else:
            return render(request, "webclient/sign-in.html", {"error": result})
    if "error" in request.GET:
        error = request.GET["error"]
    else:
        error = ""
    return render(request, "webclient/sign-in.html", {"error": error})
