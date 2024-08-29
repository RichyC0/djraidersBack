from user.models import PersonRole

class PersonRolRepository:
  def register(self, personRole):
    return PersonRole.save(personRole)
  