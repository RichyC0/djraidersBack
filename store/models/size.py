from django.db import models
from .sizeType import SizeType

class Size(models.Model):
  id = models.AutoField(primary_key = True)
  size = models.CharField(max_length = 5)
  sizeType = models.ForeignKey(SizeType, on_delete = models.DO_NOTHING)
  
  class Meta:
    db_table = 'size'