from django.views.decorators.http import require_http_methods
from ..services import ProductService
from app.exceptions import GlobalException
from django.http import JsonResponse, HttpResponse
import json

@require_http_methods(['POST', 'OPTIONS'])
def registerProduct(request, categoryId):
  try:
    if request.method != 'OPTIONS':
      productService = ProductService()
      body = json.loads(request.body)
      return JsonResponse(data = {"id": productService.register(body, categoryId) }, status = 201)
    else:
      return JsonResponse({}, status = 200)
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
  
@require_http_methods(['PATCH', 'OPTIONS'])
def updateProduct(request, categoryId, productId):
  try:
    if request.method != 'OPTIONS':
      productService = ProductService()
      body = json.loads(request.body)
      productService.update(productId, categoryId, body)
      return JsonResponse({}, status = 200, safe = False)
    else:
      return JsonResponse({}, status = 200)
  except GlobalException as e:
    return JsonResponse(status = e.status_code, safe = False, data = {"code": e.message})
  except Exception as ex:
    return JsonResponse(status = 500, safe = False, data = {"code": "INTERNAL_SERVER_ERROR"})
  
def isOptionsMethod(request):
  if request.method == 'OPTIONS':
    response = HttpResponse(status=200)
    response['Allow'] = 'GET, PATCH, POST, OPTIONS'
    return response
  