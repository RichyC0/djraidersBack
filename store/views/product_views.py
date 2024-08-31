from django.views.decorators.http import require_http_methods
from ..services import ProductService
from app.exceptions import GlobalException
from django.http import JsonResponse
import json

@require_http_methods(['POST'])
def registerProduct(request, categoryId):
  try:
    productService = ProductService()
    body = json.loads(request.body)
    return JsonResponse(data = {"id": productService.register(body, categoryId) }, status = 201)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['GET'])
def getAllProduct(request):
  try:
    productService = ProductService()
    return JsonResponse(productService.getAll(), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['GET'])
def getAllByCategory(request, categoryId):
  try:
    productService = ProductService()
    return JsonResponse(productService.getAllByCategory(categoryId), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})

@require_http_methods(['GET'])
def getById(request, id):
  try:
    productService = ProductService()
    return JsonResponse(productService.getById(id), status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
@require_http_methods(['PATCH'])
def updateProduct(request, categoryId, productId):
  try:
    productService = ProductService()
    body = json.loads(request.body)
    productService.update(productId, categoryId, body)
    return JsonResponse({}, status = 200, safe = False)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  