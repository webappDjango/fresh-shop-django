from django.db import models
from django.core.validators import RegexValidator


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

    def Sign_up(username: str, email: str, password: str, phone: str):
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
        return "Successfully"
    