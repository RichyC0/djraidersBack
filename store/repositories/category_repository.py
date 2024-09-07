from ..models import Category
from django.db.models import F

class CategoryRepository:
  
  def register(self, user):
    return Category.save(user)
  
  def getAll(self):
    return Category.objects.values('uuid', 'name', 'description', 'sizeType')
  
  def getById(self, id):
    return Category.objects.filter(uuid = id).values('uuid', 'name', 'description', 'sizeType_id').first()
  
  def save(self, category):
    category.save()
  
  def get(self, id):
    return Category.objects.get(uuid = id)