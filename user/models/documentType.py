from django.db import models

class DocumentType(models.Model):
  id = models.AutoField(primary_key = True)
  code = models.CharField(max_length = 5, null = False)
  name = models.CharField(max_length = 40, null = False)

  class Meta:
    db_table = 'document_type'