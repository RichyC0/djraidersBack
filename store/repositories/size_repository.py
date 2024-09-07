from ..models import Size
from django.db.models import Q

class SizeRepository:
  def get(self, id):
    return Size.objects.get(id=id)
  
  def getById(self, sizeTypeId, sizeId):
    return Size.objects.filter(Q(id = sizeId) & Q(sizeType = sizeTypeId)).values().first()
  
  def getAllByCategory(self, categoryId):
    return Size.objects.filter(sizeType__category__id= categoryId).values('id', 'size')