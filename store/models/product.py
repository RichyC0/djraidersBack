from django.db import models
from .brand import Brand
from .size import Size
from .category import Category
from .sizeGender import SizeGender

class Product(models.Model):
  id = models.AutoField(primary_key = True)
  name = models.CharField(max_length = 100)
  brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, null=False)
  size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, null=False)
  color = models.CharField(max_length= 50)
  price = models.IntegerField()
  state = models.CharField(
    max_length=20,
    choices=[
      ('CREATED', 'created'),
      ('AVAILABLE', 'available'),
      ('NOT_AVAILABLE', 'not_available'),
      ('OUT_OF_STOCK', 'out_of_stoke')
    ]
  )
  sizeGender = models.ForeignKey(SizeGender, on_delete = models.DO_NOTHING)
  category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=False)
  created_at = models.DateField(auto_now_add = True)
  updated_at = models.DateField(auto_now = True)
  
  class Meta:
    db_table = 'product'