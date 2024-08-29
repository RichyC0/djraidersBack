from user.models import Person

class PersonRepository:
  def register(self, person):
    return Person.save(person)