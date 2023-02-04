from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
import product.models as productModels
# Create your views here.
def gallery(request: HttpRequest):

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
    return render(request, "product/gallery.html", {"product":products})


def shop_detail(request: HttpRequest):
    if "productid" in request.GET:
        product = productModels.Product.objects.get(id=request.GET["productid"])
    else:
        return render(request, "product/error.html")
    return render(request, "product/shop-detail.html", {"product":product})