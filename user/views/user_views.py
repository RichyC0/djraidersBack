from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from user.services import UserService
from app.exceptions import GlobalException
import json

@require_http_methods(['POST'])
def registerUser(request):
  try:
    userService = UserService()
    body = json.loads(request.body)
    return JsonResponse(data = {"id": userService.register(body) }, status = 201)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['POST'])
def registerClient(request):
  try:
    userService = UserService()
    body = json.loads(request.body)
    return JsonResponse(data = {"id": userService.register(body, True) }, status = 201)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['GET'])
def getAllUsers(request):
  try:
    userService = UserService()
    return JsonResponse(userService.getAll(), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['PATCH', 'OPTIONS'])
def updatePerson(request, personId):
  try:
    if request.method != 'OPTIONS':
      userService = UserService()
      body = json.loads(request.body)
      userService.update(personId, body)
      return JsonResponse({}, status = 204)
    else:
      return JsonResponse({}, status = 200)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['GET'])
def getUser(request, personId):
  try:
    userService = UserService()
    return JsonResponse(userService.getUser(personId), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  