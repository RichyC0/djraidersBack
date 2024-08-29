from django.db import models

class Role(models.Model):
  id = models.AutoField(primary_key = True)
  code = models.CharField(max_length=20)
  name = models.CharField(max_length=20, null = False)

  class Meta:
    db_table = 'role'