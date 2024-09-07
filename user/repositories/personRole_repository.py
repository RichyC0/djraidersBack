from user.models import PersonRole

class PersonRolRepository:
  def register(self, personRole):
    return PersonRole.save(personRole)
  
  def getAllPersonRole(self, personId):
    return PersonRole.objects.select_related('person').filter(person__uuid = personId).values('id', 'role_id')