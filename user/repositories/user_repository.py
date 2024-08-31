from user.models import User
from django.db.models import F, Value

class UserRepository:
  def register(self, user):
    return User.save(user)
  
  def getAll(self):
    return User.objects.select_related(
      'person__documentType',
      'person__personrole__role'
    ).annotate(
      uuid = F('person__uuid'),
      firstName = F('person__firstName'),
      secondName = F('person__secondName'),
      lastName = F('person__lastName'),
      surName = F('person__surName'),
      documentType = F('person__documentType__name'),
      role = F('person__personrole__role__name')
    ).exclude(
      person__personrole__role__code = 'SUPERADMIN'
    ).values('uuid', 'firstName', 'secondName', 'lastName', 'surName', 'documentType', 'changePassword', 'role')

  
  
  
