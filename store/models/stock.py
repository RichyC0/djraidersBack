from user.models import User
from django.db import models
from .product import Product

class Stock(models.Model):
  id = models.AutoField(primary_key = True)
  productId = models.ForeignKey(Product, on_delete = models.DO_NOTHING)
  quantity = models.IntegerField()
  productId = models.ForeignKey(User, on_delete = models.DO_NOTHING)
  created_at = models.DateField(auto_now_add = True)
  updated_at = models.DateField(auto_now = True)
  
class Meta:
    db_table = 'stock'