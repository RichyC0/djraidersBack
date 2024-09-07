from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, person):
    token = super().get_token(person)

    token['email'] = person.email
    token['firstName'] = person.firstName
    token['lastName'] = person.lastName
    token['requireChangePassword'] = person.user.changePassword
    roles = person.personrole_set.all().select_related('role')
    token['roles'] = [role.role.name for role in roles]
    token['user_id'] = str(person.uuid) 

    return token
