from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from user.services.role_service import RoleService
import json
from app.exceptions import GlobalException

@require_http_methods(['GET'])
def getAllRoles(request):
  roleService = RoleService()
  return JsonResponse(roleService.getAll(), status = 200, safe = False)

@require_http_methods(['GET'])
def getAllPersonRoles(request, personId):
  roleService = RoleService()
  return JsonResponse(roleService.getAllUserRole(personId), status = 200, safe = False)

@require_http_methods(['POST'])
def assigRole(request):
  try:
    roleService = RoleService()
    body = json.loads(request.body)
    roleService.assignRole(body)
    return JsonResponse(data = {}, status = 201)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"}) 


