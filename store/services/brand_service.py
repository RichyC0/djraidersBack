from ..repositories import BrandRepository
from ..models import Brand
from app.exceptions import GlobalException

class BrandService:
  def __init__(self):
    self.brandRepository = BrandRepository()
    
  def get(self, id):
    try:
      return self.brandRepository.get(id)
    except Brand.DoesNotExist:
      raise GlobalException('BRAND_ID_NOT_VALID', 404)
    
  def getById(self, id):
    data = self.brandRepository.getById(id)
    if not data:
      raise GlobalException('BRAND_ID_NOT_VALID', 404)
    return data
  
  def getAll(self):
    data = self.brandRepository.getAll()
    return list(data) if data.exists() else []