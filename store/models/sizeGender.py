from django.db import models

class SizeGender(models.Model):
  id = models.AutoField(primary_key = True)
  code = models.CharField(max_length = 10)
  name = models.CharField(max_length = 30)
  
  class Meta:
    db_table = 'size_gender'