from django.db import models
# from django.contrib.auth.models import User
# from core.models import CustomUser

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    img = models.ImageField(upload_to='item_images', blank=True, null=True)

    def __str__(self) -> str:
        return self.name
