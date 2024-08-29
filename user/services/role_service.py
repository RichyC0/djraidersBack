from user.repositories.role_repository import RoleRepository

class RoleService:
  def __init__(self):
    self.roleRepository = RoleRepository()
    
  def getAll(self):
    data = self.roleRepository.getAll()
    return list(data) if data.exists() else []
