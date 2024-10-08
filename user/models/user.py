from .person import Person
from django.db import models

class User(models.Model):
  id = models.AutoField(primary_key = True)
  person = models.OneToOneField(Person, on_delete = models.DO_NOTHING)
  state = models.CharField(
    max_length = 20,
    choices = [
      ('CREATED', 'created'),
      ('ACTIVE', 'active'),
      ('INACTIVE', 'inactive'),
      ('DELETED', 'deleted')
    ],
    default = 'CREATED'
  ),
  changePassword = models.BooleanField(default = True)
  created_at = models.DateTimeField(auto_now_add = True, null = True)
  updated_at = models.DateTimeField(auto_now = True, null = True)
  
  class Meta:
    db_table = 'user'
