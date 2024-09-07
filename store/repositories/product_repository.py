from ..models import Product
from django.db.models import F

class ProductRepository:
  
  def __init__(self):
    self.values = ['uuid', 'name', 'product_description', 'brandName', 'sizeName','color', 'price', 'state', 'categoryName', 'size_gender']
    
  def register(self, product):
    return Product.save(product)
  
  def getAll(self):
    querySet = self.getAllQuery()
    return querySet.values(*self.values)
  
  def getAllByCategory(self, categoryId):
    querySet = self.getAllQuery()
    return querySet.filter(category__uuid = categoryId).values(*self.values)
  
  def getById(self, uuid):
    return Product.objects.select_related('category').filter(uuid = uuid).annotate(
     categoryId = F('category__uuid') 
    ).values(
      'uuid',
      'name',
      'description',
      'color',
      'price',
      'state',
      'brand_id',
      'categoryId',
      'size_id', 
      'sizeGender_id'
      ).first()
  
  def get(self, uuid):
    return Product.objects.get(uuid = uuid)
  
  def save(self, product):
    product.save()
    
  def getAllQuery(self):
    return Product.objects.select_related(
      'category',
      'brand',
      'size',
      'sizeGender'
    ).annotate(
      categoryName = F('category__name'),
      product_description = F('description'),
      brandName = F('brand__name'),
      sizeName = F('size__size'),
      size_gender = F('sizeGender__name')
    )