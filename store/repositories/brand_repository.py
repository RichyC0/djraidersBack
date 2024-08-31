from ..models import Brand

class BrandRepository:
  def get(self, id):
    return Brand.objects.get(id=id)