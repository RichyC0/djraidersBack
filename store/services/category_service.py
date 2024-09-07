from ..repositories import CategoryRepository
from ..models import Category
from app.exceptions import GlobalException
from django.core.exceptions import ValidationError
from .sizeType_service import SizeTypeService

class CategoryService:
  def __init__(self):
    self.categoryRepository = CategoryRepository()
    self.sizeTypeService = SizeTypeService()
    
  def getAll(self):
    data = self.categoryRepository.getAll()
    return list(data) if data.exists() else []
  
  def register(self, category):
    categoryModel = Category(
      name= category.get('name'),
      sizeType = self.sizeTypeService.get(category.get('sizeType_id')),
      description = category.get('description')
    )
    self.categoryRepository.register(categoryModel)
    return categoryModel.uuid
  
  def update(self, uuid, category):
    categoryModel = self.get(uuid)
    categoryModel.name = category.get('name')
    categoryModel.description = category.get('description')
    categoryModel.sizeType = self.sizeTypeService.get(category.get('sizeType_id'))
    self.categoryRepository.save(categoryModel)

  def getCategory(self, uuid):
    data = self.categoryRepository.getById(uuid)
    if not data:
      raise GlobalException("CATEGORY_ID_NOT_VALID", 404)
    return data
  
  def get(self, uuid):
    try:
      return self.categoryRepository.get(uuid)
    except Category.DoesNotExist:
      raise GlobalException("CATEGORY_ID_NOT_VALID", 404)
    