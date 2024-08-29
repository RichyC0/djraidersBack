
from django.db import models

class Category(models.Model):
  id = models.AutoField(primary_key = True)
  name = models.CharField(max_length = 100)
  description = models.TextField(null=False)
  created_at = models.DateField(auto_now_add = True)
  updated_at = models.DateField(auto_now = True)
  
  class Meta:
    db_table = 'category'