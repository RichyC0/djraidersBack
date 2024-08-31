from ..repositories import UserRepository, PersonRepository, DocumentTypeRepository, ClientRepository
from ..models.user import Person, User
from ..models.client import Client
from ..models.documentType import DocumentType
from app.exceptions import GlobalException
from django.db import IntegrityError
import environ

env = environ.Env()

class UserService:
  def __init__(self):
    self.userRepository = UserRepository()
    self.personRepository = PersonRepository()
    self.documentTypeRepository = DocumentTypeRepository()
    self.clientRepository = ClientRepository()
    self.secretPassword = env('GENERIC_PASSWORD')
    
  def register(self, user, isClient = False):
    person = self.savePerson(user, isClient)
    if isClient == True:
      self.saveClient(user, person)
    else: 
      self.saveUser(person) 
    return person.uuid
    
  def savePerson(self, person, isClient):
    try:
      person = Person(
        documentType = self.getDocumentType(person.get("documentType")),
        firstName = person.get("firstName"),
        secondName = person.get("secondName"),
        lastName = person.get("lastName"),
        surName = person.get ("surName"),
        documentNumber = person.get("documentNumber"),
        email = person.get("email"),
        password = self.secretPassword if isClient == False else person.get("password")
      )
      self.personRepository.register(person)
      return person
    except IntegrityError:
      raise GlobalException("USER_ALREADY_EXIST")
      
  def saveUser(self, person):
    user = User(person = person)
    self.userRepository.register(user)
    
  def saveClient(self, user, person):
    client = Client(
      person = person,
      birthday = user.get("birthday"),
      address = user.get("address"),
      cellphone = user.get("cellphone")
    )
    self.clientRepository.register(client)
    
  def getDocumentType(self, documentTypeId):
    try:
      return self.documentTypeRepository.get(documentTypeId)
    except DocumentType.DoesNotExist:
      raise GlobalException("NOT_VALID_DOCUMENTTYPE")
  
  def getAll(self):
    data = self.userRepository.getAll()
    return list(data)