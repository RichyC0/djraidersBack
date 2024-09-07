from user.models import Person
from django.db.models import F
class PersonRepository:
  def register(self, person):
    return Person.save(person)
  
  def getByUUID(self, uuid):
    return Person.objects.get(uuid = uuid)
  
  def save(self, product):
    product.save()