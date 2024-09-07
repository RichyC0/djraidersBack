from .size_service import SizeService
from ..repositories import ProductRepository
from ..models import Product
from app.exceptions import GlobalException
from django.core.exceptions import ValidationError
from .category_service import CategoryService
from .brand_service import BrandService
from .sizeGender_service import SizeGenderService

class ProductService:
  def __init__(self):
    self.productRepository = ProductRepository()
    self.categoryService = CategoryService()
    self.sizeService = SizeService()
    self.sizeGenderService = SizeGenderService()
    self.brandService = BrandService()
    
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
      brand = self.brandService.get(product.get('brand_id')),
      size = self.sizeService.get(product.get('size_id')),
      color = product.get('color'),
      price = product.get('price'),
      category = self.categoryService.get(categoryId),
      sizeGender = self.sizeGenderService.get(product.get('sizeGender_id'))
    )
    self.productRepository.register(productModel)
    return productModel.uuid
  
  def getById(self, uuid):
    try:
      return self.productRepository.getById(uuid)
    except (Product.DoesNotExist, ValidationError):
      raise GlobalException('PRODUCT_ID_NOT_VALID', 404)
  
  def update(self, uuid, categoryId, product):
    productModel = self.productRepository.get(uuid)
    productModel.name = product.get('name') if product.get('name') != None else productModel.name
    productModel.description = product.get('description') if product.get('description') != None else productModel.description
    productModel.brand = self.brandService.get(product.get('brand_id'))
    productModel.size = self.sizeService.get(product.get('size_id'))
    productModel.color = product.get('color') if product.get('color') != None else productModel.color
    productModel.price = product.get('price') if product.get('price') != None else productModel.price
    productModel.category = self.categoryService.get(categoryId)
    productModel.sizeGender = self.sizeGenderService.get(product.get('sizeGender_id'))
    self.productRepository.save(productModel)
    
