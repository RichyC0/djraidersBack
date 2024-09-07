from ..models import Brand

class BrandRepository:
  def get(self, id):
    return Brand.objects.get(id = id)
  
  def getById(self, id):
    return Brand.objects.filter(id=id).values().first()
  
  def getAll(self):
    return Brand.objects.all().values('id', 'name')
  