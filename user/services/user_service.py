from user.repositories.user_repository import UserRepository
from user.repositories.person_repository import PersonRepository
from user.repositories.documentType_repository import DocumentTypeRepository
from ..models.user import Person, User
from ..models.documentType import DocumentType
from ..exceptions.global_exception import GlobalException
from django.db import IntegrityError
import environ

env = environ.Env()

class UserService:
  def __init__(self):
    self.userRepository = UserRepository()
    self.personRepository = PersonRepository()
    self.documentTypeRepository = DocumentTypeRepository()
    self.secretPassword = env('GENERIC_PASSWORD')
    
  def register(self, user):
    person = self.savePerson(user)
    self.saveUser(person)  
    return person.uuid
  
  def savePerson(self, person):
    try:
      person = Person(
        documentType = self.getDocumentType(person.get("documentType")),
        firstName = person.get("firstName"),
        secondName = person.get("secondName"),
        lastName = person.get("lastName"),
        surName = person.get ("surName"),
        documentNumber = person.get("documentNumber"),
        email = person.get("email"),
        password = self.secretPassword
      )
      self.personRepository.register(person)
      return person
    except IntegrityError:
      raise GlobalException("USER_ALREADY_EXIST")
      
  def saveUser(self, person):
    self.personRepository.register(person)
    user = User(person = person)
    self.userRepository.register(user)
    
  def getDocumentType(self, documentTypeId):
    try:
      return self.documentTypeRepository.get(documentTypeId)
    except DocumentType.DoesNotExist:
      raise GlobalException("NOT_VALID_DOCUMENTTYPE")
  