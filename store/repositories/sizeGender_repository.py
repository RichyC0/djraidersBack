from ..models import SizeGender

class SizeGenderRepository:
  def get(self, id):
    return SizeGender.objects.get(id=id)