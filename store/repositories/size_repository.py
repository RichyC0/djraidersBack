from ..models import Size

class SizeRepository:
  def get(self, id):
    return Size.objects.get(id=id)