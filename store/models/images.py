from django.db import models
import uuid

class Images(models.Model):
  id = models.AutoField(primary_key = True)
  uuid = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
  route = models.TextField()
  
class Meta:
    db_table = 'images'