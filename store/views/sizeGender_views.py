from django.views.decorators.http import require_http_methods
from ..services import SizeGenderService
from app.exceptions import GlobalException
from django.http import JsonResponse

@require_http_methods(['GET'])
def getAllSizeGenders(request):
  try:
    sizeGenderService = SizeGenderService()
    return JsonResponse(sizeGenderService.getAll(), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['GET'])
def getById(request, id):
  try:
    sizeGenderService = SizeGenderService()
    return JsonResponse(sizeGenderService.getById(id), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})