from user.models import User

class UserRepository:
  def register(self, user):
    return User.save(user)