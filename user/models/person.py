from .documentType import DocumentType
from django.db import models
import uuid

class Person(models.Model):
  id = models.AutoField(primary_key = True)
  uuid = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
  documentType = models.ForeignKey(DocumentType, null = False, on_delete = models.DO_NOTHING)
  firstName = models.CharField(max_length = 25, null = False)
  secondName = models.CharField(max_length = 25, null = True)
  lastName = models.CharField(max_length = 25, null = False)
  surName = models.CharField(max_length = 25, null = True)
  documentNumber =models.CharField( max_length = 25, null = False)
  email= models.EmailField(unique = True, null = False)
  password = models.CharField(max_length = 200)
 
  class Meta:
    db_table = 'person'