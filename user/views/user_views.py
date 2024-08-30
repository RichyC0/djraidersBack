from django.http import JsonResponse
from user.services.user_service import UserService
import json
from ..exceptions.global_exception import GlobalException

def registerUser(request):
  try:
    userService = UserService()
    body = json.loads(request.body)
    return JsonResponse(data = {"id": userService.register(body) }, status = 201)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
def registerClient(request):
  try:
    userService = UserService()
    body = json.loads(request.body)
    return JsonResponse(data = {"id": userService.register(body, True) }, status = 201)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
def getAllUsers(request):
  try:
    userService = UserService()
    return JsonResponse(userService.getAll(), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})