from django.http import JsonResponse
from user.services.user_service import UserService
import json
from ..exceptions.global_exception import GlobalException

def registerUser(request):
  try:
    userService = UserService()
    body = json.loads(request.body)
    userService.register(body)
    return JsonResponse(data = {}, status = 201)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    print(ex)
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})