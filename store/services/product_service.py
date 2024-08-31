from ..repositories import ProductRepository, CategoryRepository, SizeRepository, SizeGenderRepository, BrandRepository
from ..models import Product, Category, Size, SizeGender, Brand
from app.exceptions import GlobalException

class ProductService:
  def __init__(self):
    self.productRepository = ProductRepository()
    self.categoryRepository = CategoryRepository()
    self.sizeRepository = SizeRepository()
    self.sizeGenderRepository = SizeGenderRepository()
    self.brandRepository = BrandRepository()
    
  def getAll(self):
    data = self.productRepository.getAll()
    return list(data) if data.exists() else []
  
  def getAllByCategory(self, uuid):
    data = self.productRepository.getAllByCategory(uuid)
    return list(data) if data.exists() else []
  
  def register(self, product, categoryId):
    productModel = Product(
      name = product.get('name'),
      description = product.get('description'),
      brand = self.getBrand(product.get('brandId')),
      size = self.getSize(product.get('sizeId')),
      color = product.get('color'),
      price = product.get('price'),
      category = self.getCategory(categoryId),
      sizeGender = self.getSizeGender(product.get('sizeGenderId'))
    )
    self.productRepository.register(productModel)
    return productModel.uuid
  
  def getById(self, uuid):
    try:
      return self.productRepository.getById(uuid)
    except Product.DoesNotExist:
      raise GlobalException('PRODUCT_ID_NOT_VALID')
  
  def update(self, uuid, categoryId, product):
    productModel = self.productRepository.get(uuid)
    productModel.name = product.get('name') if product.get('name') != None else productModel.name
    productModel.description = product.get('description') if product.get('description') != None else productModel.description
    productModel.brand = self.getBrand(product.get('brandId'))
    productModel.size = self.getSize(product.get('sizeId'))
    productModel.color = product.get('color') if product.get('color') != None else productModel.color
    productModel.price = product.get('price') if product.get('price') != None else productModel.price
    productModel.category = self.getCategory(categoryId)
    productModel.sizeGender = self.getSizeGender(product.get('sizeGenderId'))
    self.productRepository.save(productModel)
    
  def getCategory(self, uuid):
    try:
      return self.categoryRepository.getById(uuid)
    except Category.DoesNotExist:
      raise GlobalException("CATEGORY_ID_NOT_VALID")
    
  def getBrand(self, id):
    try:
      return self.brandRepository.get(id)
    except Brand.DoesNotExist:
      raise GlobalException("BRAND_ID_NOT_VALID")
    
  def getSize(self, id):
    try:
      return self.sizeRepository.get(id)
    except Size.DoesNotExist:
      raise GlobalException("SIZE_ID_NOT_VALID")
  
  def getSizeGender(self, id):
    try:
      return self.sizeGenderRepository.get(id)
    except SizeGender.DoesNotExist:
      raise GlobalException("SIZEGENDER_ID_NOT_VALID")
    
    
    