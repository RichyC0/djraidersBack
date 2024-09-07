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
  
  def update(self, uuid, person):
    personModel = self.personRepository.getByUUID(uuid)
    personModel.firstName = person.get('firstName') if person.get('firstName') != None else personModel.firstName
    personModel.secondName = person.get('secondName') if person.get('secondName') != None else personModel.secondName
    personModel.lastName = person.get('lastdName') if person.get('lastName') != None else personModel.lasttName
    personModel.lastName = person.get('surName') if person.get('surName') != None else personModel.surName
    personModel.documentNumber = person.get('documentNumber') if person.get('documentNumber') != None else personModel.documentNumber
    personModel.email = person.get('email') if person.get('email') != None else personModel.email
    personModel.documentType = person.get('documentType_id')
    self.personRepository.save(personModel)
    
  def getUser(self, uuid):
    data = self.userRepository.getUser(uuid)
    if not data:
      raise GlobalException("USER_NOT_FOUND")
    return data