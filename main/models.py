from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(null=True)

    def _str_(self):
        return self.user.username

class ProductCategory(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)

    def _str_(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)
    price=models.FloatField()

    def _str_(self):
        return self.title