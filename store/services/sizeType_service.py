from ..repositories import SizeTypeRepository
from app.exceptions import GlobalException
from ..models import SizeType

class SizeTypeService:
  def __init__(self):
    self.sizeTypeRepository = SizeTypeRepository()
    
  def getById(self, id):
    data = self.sizeTypeRepository.getById(id)
    if not data:
      raise GlobalException('SIZETYPE_ID_NOT_VALID', 404)
    return data
  
  def get(self, id):
    try:
      return self.sizeTypeRepository.get(id)
    except SizeType.DoesNotExist:
      raise GlobalException('SIZETYPE_ID_NOT_VALID', 404)
    
  def getAll(self):
    data = self.sizeTypeRepository.getAll()
    return list(data) if data.exists() else []