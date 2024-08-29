from django.db import models

class Client(models.Model):
  id = models.AutoField(primary_key = True)
  birthday= models.DateField(null = False)
  address = models.CharField(max_length = 25, null = False)
  cellphone = models.CharField(max_length = 10, null = False)
  created_at = models.DateField(auto_now_add = True)
  updated_at = models.DateField(auto_now = True)
  
  class Meta:
    db_table = 'client'