from django.db import models
from .product import Product
from .images import Images

class PrudctoImages(models.Model):
  id = models.AutoField(primary_key = True)
  personId = models.ForeignKey(Product, on_delete = models.DO_NOTHING)
  roleId = models.ForeignKey(Images, on_delete = models.DO_NOTHING)
  
  class Meta:
    db_table = 'product_images'