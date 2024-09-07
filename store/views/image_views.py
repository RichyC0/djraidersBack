# views.py

import base64
from io import BytesIO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cloudinary.uploader
import cloudinary.api
import json

@csrf_exempt
def uploadFile(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    resultados = []

    for imagen_obj in data['imagenes']:
      base64_img = imagen_obj['base64']
      nombre_archivo = imagen_obj['nombre']
      tipo_archivo = imagen_obj['tipo']

      formato_imagen = tipo_archivo.split('/')[1].split(';')[0]
      img_data = base64.b64decode(base64_img.split(',')[1])
      img_io = BytesIO(img_data)
      response = cloudinary.uploader.upload(img_io, filename=nombre_archivo, resource_type='image', format=formato_imagen)
      resultados.append(
        {
          'url': response['secure_url'],
          'public_id': response['public_id'],
          'nombre': nombre_archivo,
          'formato': formato_imagen
        }
      )
    return JsonResponse({'resultados': resultados})
  return JsonResponse({'error': 'Método no permitido'}, status=405)
