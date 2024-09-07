from django.views.decorators.http import require_http_methods
from ..services import BrandService
from app.exceptions import GlobalException
from django.http import JsonResponse
import json

@require_http_methods(['GET'])
def getAllBrands(request):
  try:
    brandService = BrandService()
    return JsonResponse(brandService.getAll(), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['GET'])
def getById(request, id):
  try:
    brandService = BrandService()
    return JsonResponse(brandService.getById(id), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})