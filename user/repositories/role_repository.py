from user.models import Role

class RoleRepository:
  def getAll(self):
    return Role.objects.values('id', 'code', 'name')
  
  def getById(self, id):
    return Role.objects.get(id = id)