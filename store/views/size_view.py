from django.views.decorators.http import require_http_methods
from ..services import SizeService
from app.exceptions import GlobalException
from django.http import JsonResponse

@require_http_methods(['GET'])
def getAllBySizeType(request, categoryId):
  try:
    sizeService = SizeService()
    return JsonResponse(sizeService.getAllByCategory(categoryId), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['GET'])
def getById(request, sizeTypeId, sizeId):
  try:
    sizeService = SizeService()
    return JsonResponse(sizeService.getById(sizeTypeId, sizeId), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})