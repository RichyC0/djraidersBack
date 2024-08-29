from django.db import models

class Size(models.Model):
  id = models.AutoField(primary_key = True)
  size = models.CharField(max_length = 5)
  
  class Meta:
    db_table = 'size'