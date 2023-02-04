from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse, HttpResponse
from Admin.models import admin
from product import models

def _CheckAccessing(request: HttpRequest):
    if "AdminId" in request.POST:
        return request.POST["AdminId"]
    else:
        return None
# Create your views here.
def index(request:HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("Login?error=Sign in first")

    return allProduct(request)

def Check(request: HttpRequest):
    email = request.POST["email"]
    password = request.POST["password"]
    ad = admin.CheckLogin(email, password)
    if ad is not None:
        request.session['AdminId'] = ad.id
    return HttpResponseRedirect("Login")

def Login(request: HttpRequest):
    if _CheckAccessing(request):
        return HttpResponseRedirect("index")
        
    if "error" in request.GET:
        error = request.GET["error"]
    else:
        error = ""
    return render(request, "login.html", {"error":error})

def addProduct(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("Login?error=Sign in first")

    categories = models.Category.objects.all()
    return render(request, "addProduct.html", {"categories":categories})

def allCategory(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("Login?error=Sign in first")

    categories = models.Category.objects.all()
    return render(request, "allCategory.html", {"categories":categories})

def addCategory(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("Login?error=Sign in first")

    if "Add" in request.GET:
        nameCate = request.GET["name"]
        models.Category.Add(nameCate)
    categories = models.Category.objects.all()
    return render(request, "addCategory.html", {"categories":categories})

def editCategory(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("Login?error=Sign in first")

    if "Delete" in request.GET:
        id = request.GET["id"]
        models.Category.Delete(id)
    if "Edit" in request.GET:
        category = models.Category.objects.get(id=request.GET["id"])
        category.name = request.GET["name"]
        category.save(force_update=True)
    categories = models.Category.objects.all()
    return render(request, "editCategory.html", {"categories":categories})

def allProduct(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("Login?error=Sign in first")

    categories = models.Category.objects.all()
    products = models.Product.objects.all()
    return render(request, "allProduct.html", {"categories":categories, "products":products})

def addProduct(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("Login?error=Sign in first")

    if "Add" in request.GET:
        name = request.GET["name"]
        cate_id = request.GET["cate_id"]
        description = request.GET["description"]
        price = request.GET["price"]
        amount = request.GET["amount"]
        image = request.GET["image"]
        models.Product.Add(name, cate_id, description, price, amount, image)
    categories = models.Category.objects.all()
    products = models.Product.objects.all()
    return render(request, "addProduct.html", {"categories":categories, "products":products})

def editProduct(request: HttpRequest):
    if _CheckAccessing(request) is None:
        return HttpResponseRedirect("Login?error=Sign in first")

    if "Delete" in request.GET:
        models.Product.objects.filter(id=request.GET["id"]).delete()
    if "Edit" in request.GET:
        product = models.Product.objects.get(id=request.GET["id"])
        product.name = request.GET["name"]
        product.cate_id = models.Category.objects.get(name=request.GET["category"])
        product.description = request.GET["description"]
        product.price = request.GET["price"]
        product.remain = request.GET["remain"]
        product.initAmount = request.GET["initAmount"]
        product.image = request.GET["image"]
        product.save(force_update=True)
    categories = models.Category.objects.all()
    products = models.Product.objects.all()
    return render(request, "editProduct.html", {"categories":categories, "products":products})

#ajax
def getCategory(request: HttpRequest):
    cate_id = request.GET["cate_id"]
    category = models.Category.objects.get(id=cate_id)
    return render(request, "Ajax/category.html", {"category":category})
    
def getProduct(request: HttpRequest):
    product_id = request.GET["product_id"]
    product = models.Product.objects.get(id=product_id)
    return render(request, "Ajax/product.html", {"product":product, "imgPath": product.GetPathImg()})
    