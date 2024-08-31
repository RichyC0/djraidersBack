from ..models import Category
from django.db.models import F

class CategoryRepository:
  
  def register(self, user):
    return Category.save(user)
  
  def getAll(self):
    return Category.objects.select_related('sizeType').annotate(
      size_type = F('sizeType__name'),
    ).values('uuid', 'name', 'description', 'size_type')
  
  def getById(self, id):
    return Category.objects.get(uuid = id)
  
  def save(self, category):
    category.save()