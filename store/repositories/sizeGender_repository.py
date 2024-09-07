from ..models import SizeGender

class SizeGenderRepository:
  def getById(self, id):
    return SizeGender.objects.filter(id=id).values().first()
  
  def get(self, id):
    return SizeGender.objects.get(id=id)
  
  def getAll(self):
    return SizeGender.objects.all().values()