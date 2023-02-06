from django.db import models
from django.core.validators import RegexValidator
from product.models import Product

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    username = models.CharField(max_length=30)

    phone_regex = RegexValidator(regex='\d*', message="Trường này chỉ dùng cho kiểu số.")
    phone = models.CharField(validators=[phone_regex],max_length=12)
    avatar = models.CharField(max_length=255)

    def CheckLogin(email: str, password: str):
        try:
            user = User.objects.get(email=email, password=password)
        except:
            user = "email or password is wrong"
        return user

    def Sign_up(username: str, email: str, password: str, repassword: str, phone: str):
        avatar = "webclient\\Defaut-avatar.jpg"
        user = User()
        user.username = username
        user.email = email
        user.password = password
        user.phone = phone
        user.avatar = avatar
        if User.objects.filter(email=email).count() > 0:
            return "This email have been used"
        else:
            user.save(True)
            cart = Cart(user=user)
            cart.save(True)
        return "Successfully"
    
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name="cart")
    products = models.ManyToManyField(Product, blank=True, related_name="carts")

    def AddtoCart(self, product: Product):
        if self.products.filter(id = product.id).count() == 0:
            self.products.add(product)
            return "Successfully! Added product to your cart."
        else:
            return "Failed! This product have been in your cart."
        