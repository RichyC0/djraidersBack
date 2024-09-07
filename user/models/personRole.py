from django.db import models
from .person import Person
from .role import Role

class PersonRole(models.Model):
  id = models.AutoField(primary_key = True)
  person = models.ForeignKey(Person, on_delete = models.DO_NOTHING)
  role = models.ForeignKey(Role, on_delete = models.DO_NOTHING)
  
  class Meta:
    db_table = 'person_role'
    unique_together = ('person', 'role')