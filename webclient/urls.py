from django.urls import include,path
from webclient import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('shop', views.shop),
    path('about', views.about),
    path('cart', views.cart),
    path('checkout', views.checkout),
    path('contact_us', views.contact_us),
    path('my-account', views.my_account),
    path('wishlist', views.wishlist),
    path('sign-up', views.sign_up),
    path('sign-in', views.sign_in),
    
    path('AddtoCart', views.AddtoCart),
]
