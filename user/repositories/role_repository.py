from user.models import Role

class RoleRepository:
  def getAll(self):
    return Role.objects.values('id', 'code', 'name')