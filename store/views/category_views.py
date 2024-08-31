from django.views.decorators.http import require_http_methods
from ..services import CategoryService
from app.exceptions import GlobalException
from django.http import JsonResponse
import json

@require_http_methods(['GET'])
def getAllCategories(request):
  try:
    categoryService = CategoryService()
    return JsonResponse(categoryService.getAll(), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['POST'])
def registerCategories(request):
  try:
    categoryService = CategoryService()
    body = json.loads(request.body)
    return JsonResponse(data = {"id": categoryService.register(body) }, status = 201)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['PATCH'])
def updateCategory(request, id):
  try:
    categoryService = CategoryService()
    body = json.loads(request.body)
    categoryService.update(id, body)
    return JsonResponse({}, status = 204)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  