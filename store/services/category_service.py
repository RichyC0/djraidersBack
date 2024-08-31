from ..repositories import CategoryRepository, SizeTypeRepository
from ..models import Category, SizeType
from app.exceptions import GlobalException

class CategoryService:
  def __init__(self):
    self.categoryRepository = CategoryRepository()
    self.sizeTypeRepository = SizeTypeRepository()
    
  def getAll(self):
    data = self.categoryRepository.getAll()
    return list(data) if data.exists() else []
  
  def register(self, category):
    categoryModel = Category(
      name= category.get('name'),
      sizeType = self.getSizeType(category.get('sizeTypeId')),
      description = category.get('description')
    )
    self.categoryRepository.register(categoryModel)
    return categoryModel.uuid
  
  def update(self, uuid, category):
    categoryModel = self.getCategory(uuid)
    categoryModel.name = category.get('name')
    categoryModel.description = category.get('description')
    categoryModel.sizeType = self.getSizeType(category.get('sizeTypeId'))
    self.categoryRepository.save(categoryModel)

  def getSizeType(self, id):
    try:
      return self.sizeTypeRepository.get(id)
    except SizeType.DoesNotExist:
      raise GlobalException("SIZETYPE_ID_NOT_VALID")

  def getCategory(self, uuid):
    try:
      return self.categoryRepository.getById(uuid)
    except Category.DoesNotExist:
      raise GlobalException("CATEGORY_ID_NOT_VALID", 404)
    