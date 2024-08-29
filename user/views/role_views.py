from django.http import JsonResponse
from user.services.role_service import RoleService
import json
from ..exceptions.global_exception import GlobalException

def getAllRoles(request):
  roleService = RoleService()
  return JsonResponse(roleService.getAll(), status = 200, safe = False)

def assigRole(request):
  try:
    roleService = RoleService()
    body = json.loads(request.body)
    print(body)
    roleService.assignRole(body)
    return JsonResponse(data = {}, status = 201)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    print(ex)
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"}) 


