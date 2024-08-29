from django.http import JsonResponse
from user.services.role_service import RoleService

def getAllRoles(request):
  roleService = RoleService()
  return JsonResponse(roleService.getAll(), status = 200, safe = False)
