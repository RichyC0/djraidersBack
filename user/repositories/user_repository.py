from user.models import User
from django.db.models import F

class UserRepository:
  def register(self, user):
    return User.save(user)
  
  def getUser(self, uuid):
    return User.objects.select_related('person__personrole').annotate(
      documentType_id = F('person__documentType'),
      firstName = F('person__firstName'),
      secondName = F('person__secondName'),
      lastName = F('person__lastName'),
      surName = F('person__surName'),
      documentNumber= F('person__documentNumber'),
      email = F('person__email'),
      role_id = F('person__personrole__role_id')
    ).filter(
      person__uuid = uuid
    ).values(
      'documentType_id',
      'firstName',
      'secondName',
      'lastName',
      'surName',
      'documentNumber',
      'email',
      'role_id'
    ).first()
  
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
      documentNumber= F('person__documentNumber'),
      role = F('person__personrole__role__name')
    ).values('uuid', 'firstName', 'secondName', 'lastName', 'surName', 'documentType', 'documentNumber', 'changePassword', 'role')

  
  
  
