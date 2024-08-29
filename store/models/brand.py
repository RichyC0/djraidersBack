from django.db import models

class Brand(models.Model):
  id = models.AutoField(primary_key = True)
  name = models.CharField(max_length = 100)
  
  class Meta:
    db_table = 'Brand'