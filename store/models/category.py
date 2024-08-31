
from django.db import models
from .sizeType import SizeType
import uuid

class Category(models.Model):
  id = models.AutoField(primary_key = True)
  uuid = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
  name = models.CharField(max_length = 100)
  sizeType = models.ForeignKey(SizeType, on_delete = models.DO_NOTHING)
  description = models.TextField(null=False)
  created_at = models.DateField(auto_now_add = True)
  updated_at = models.DateField(auto_now = True)
  
  class Meta:
    db_table = 'category'