from ..repositories import SizeRepository
from ..models import Size
from app.exceptions import GlobalException
from ..services import CategoryService

class SizeService:
  def __init__(self):
    self.sizeRepository = SizeRepository()
    self.categoryService = CategoryService()
    
  def get(self, id):
    try:
      return self.sizeRepository.get(id)
    except Size.DoesNotExist:
      raise GlobalException("SIZE_ID_NOT_VALID", 404)
    
  def getById(self, sizeTypeId, sizeId):
    data = self.sizeRepository.getById(sizeTypeId, sizeId)
    if not data:
      raise GlobalException("SIZE_ID_NOT_VALID", 404)
    return data
    
  def getAllByCategory(self, categoryId):
    category = self.categoryService.get(categoryId)
    data = self.sizeRepository.getAllByCategory(category.id)
    return list(data) if data.exists() else []