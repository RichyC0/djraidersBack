from django.db import models

class Client(models.Model):
  id = models.AutoField(primary_key = True)
  birthday= models.DateField()
  address = models.CharField(max_length = 25)
  cellphone = models.CharField(max_length = 10)
  created_at = models.DateTimeField(auto_now_add = True, null = True)
  updated_at = models.DateTimeField(auto_now = True, null = True)
  
  class Meta:
    db_table = 'client'