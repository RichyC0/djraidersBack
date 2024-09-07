from ..models import SizeType

class SizeTypeRepository:
  def getById(self, id):
    return SizeType.objects.filter(id = id).values().first()

  def get(self, id):
    return SizeType.objects.get(id=id)
  
  def getAll(self):
    return SizeType.objects.all().values()