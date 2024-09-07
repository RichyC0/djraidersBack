from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from .documentType import DocumentType

class PersonManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('El campo de email debe ser establecido')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
        
    return self.create_user(email, password, **extra_fields)
  
class Person(AbstractBaseUser):
  id = models.AutoField(primary_key = True)
  uuid = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
  documentType = models.ForeignKey(DocumentType, null = False, on_delete = models.DO_NOTHING)
  firstName = models.CharField(max_length = 25, null = False)
  secondName = models.CharField(max_length = 25, null = True)
  lastName = models.CharField(max_length = 25, null = False)
  surName = models.CharField(max_length = 25, null = True)
  documentNumber =models.CharField( max_length = 25, null = False)
  email= models.EmailField(unique = True, null = False)
  password = models.CharField(max_length = 200)
  is_active = models.BooleanField(default=True)  # Para desactivar o activar la cuenta
  is_staff = models.BooleanField(default=False)  # Para dar acceso al admin
  is_superuser = models.BooleanField(default=False) 
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['firstName', 'lastName', 'documentType', 'documentNumber']
  
  objects = PersonManager()
  
  def save(self, *args, **kwargs):
    if self.pk is None or not Person.objects.get(pk=self.pk).password == self.password:
      self.password = make_password(self.password)
    super(Person, self).save(*args, **kwargs)

  def check_password(self, raw_password):
    return check_password(raw_password, self.password)
  
  @property
  def is_anonymous(self):
    # Este atributo es requerido por Django para verificar si el usuario es anónimo
    return False

  @property
  def is_authenticated(self):
    # Este atributo es requerido por Django para verificar si el usuario está autenticado
    return True
  
  class Meta:
    db_table = 'person'
