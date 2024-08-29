from user.models import User
from django.db import models
from .product import Product

class Stock(models.Model):
  id = models.AutoField(primary_key = True)
  product = models.ForeignKey(Product, on_delete = models.DO_NOTHING)
  quantity = models.IntegerField()
  user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
  created_at = models.DateField(auto_now_add = True)
  updated_at = models.DateField(auto_now = True)
  
class Meta:
    db_table = 'stock'