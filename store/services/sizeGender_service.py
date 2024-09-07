from ..repositories import SizeGenderRepository
from ..models import SizeGender
from app.exceptions import GlobalException

class SizeGenderService:
  def __init__(self):
    self.sizeGenderRepository = SizeGenderRepository()
    
  def getById(self, id):
    data = self.sizeGenderRepository.getById(id)
    if not data:
      raise GlobalException('SIZEGENDER_ID_NOT_VALID', 404)
    return data
  
  def get(self, id):
    try:
      return self.sizeGenderRepository.get(id)
    except SizeGender.DoesNotExist:
      raise GlobalException('SIZEGENDER_ID_NOT_VALID', 404)
  
  def getAll(self):
    data = self.sizeGenderRepository.getAll()
    return list(data) if data.exists() else []