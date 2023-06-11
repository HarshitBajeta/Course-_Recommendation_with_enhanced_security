from django.db import models
# from django.contrib.auth.models import User
from item.models import Item, Category
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password,hashed_password, **extra_fields):

        if not username:
            raise ValueError('User must have a valid username')
        if not email:
            raise ValueError('User must have a email')
        if not password:
            raise ValueError('User must have a password')
        # if not image:
        #     raise ValueError('User must have a image')
        
        user = self.model(username=username, email=self.normalize_email(email),hashed_password=hashed_password, **extra_fields)
        user.set_password(password)
        # user.is_active = True
        # user.is_staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username,email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    hashed_password = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='users', null=True, blank=True)

    # Add additional fields to the user model
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "password"]#, "image"]
    objects = UserManager()

    def __str__(self):
        return "@{}".format(self.username)
    
class Order(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    
class Userimage(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='users', blank=False, null=False)
    
class Order_Item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    buy_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True)

class Camera_image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='login_folder', blank=True, null=True)

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     preferred_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
