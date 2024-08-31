from ..models import SizeType

class SizeTypeRepository:
  def get(self, id):
    return SizeType.objects.get(id=id)