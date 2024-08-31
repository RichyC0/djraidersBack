from ..repositories import RoleRepository, PersonRepository, PersonRolRepository
from ..models import Person, Role, PersonRole
from app.exceptions import GlobalException

class RoleService:
  def __init__(self):
    self.roleRepository = RoleRepository()
    self.personRepository = PersonRepository()
    self.personRoleRepository = PersonRolRepository()
    
  def getAll(self):
    data = self.roleRepository.getAll()
    return list(data) if data.exists() else []
  
  def assignRole(self, body):
    rolePerson = PersonRole(
      person = self.getPerson(body.get("personId")),
      role = self.getRole(body.get("roleId"))
    )
    self.personRoleRepository.register(rolePerson)
    
  def getPerson(self, uuid):
    try:
      person = self.personRepository.getByUUID(uuid)
      return person
    except Person.DoesNotExist:
      raise GlobalException("NOT_VALID_USER")

  def getRole(self, roleid):
    try:
      role = self.roleRepository.getById(roleid)
      return role
    except Role.DoesNotExist:
      raise GlobalException("NOT_VALID_ROLE")