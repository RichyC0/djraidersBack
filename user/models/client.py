from django.db import models
from .person import Person

class Client(models.Model):
  id = models.AutoField(primary_key = True)
  person = models.ForeignKey(Person, on_delete = models.DO_NOTHING)
  birthday = models.DateField()
  address = models.CharField(max_length = 250)
  cellphone = models.CharField(max_length = 10)
  created_at = models.DateTimeField(auto_now_add = True, null = True)
  updated_at = models.DateTimeField(auto_now = True, null = True)
  
  class Meta:
    db_table = 'client'