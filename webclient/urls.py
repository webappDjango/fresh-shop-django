from django.urls import include,path
from webclient import views

urlpatterns = [
    path('', views.index),
    path('shop', views.shop),
    path('about', views.about),
    path('cart', views.cart),
    path('checkout', views.checkout),
    path('contact_us', views.contact_us),
    path('gallery', views.gallery),
    path('my_account', views.my_account),
    path('shop_detail', views.shop_detail),
    path('wishlist', views.wishlist),
]
