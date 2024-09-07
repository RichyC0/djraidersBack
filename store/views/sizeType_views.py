from django.views.decorators.http import require_http_methods
from ..services import SizeTypeService
from app.exceptions import GlobalException
from django.http import JsonResponse

@require_http_methods(['GET'])
def getAll(request):
  try:
    sizeTypeService = SizeTypeService()
    return JsonResponse(sizeTypeService.getAll(), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['GET'])
def getById(request, id):
  try:
    sizeTypeService = SizeTypeService()
    return JsonResponse(sizeTypeService.getById(id), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})