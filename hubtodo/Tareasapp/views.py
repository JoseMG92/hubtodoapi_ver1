from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Tareasapp.models import Tareas
from Tareasapp.serializers import TareasSerializer
# Create your views here.

@csrf_exempt
def tareas_api(request,id=0):
    if request.method == 'GET':
        tarea = Tareas.objects.all()
        tarea_serializer = TareasSerializer(tarea,many=True)
        return JsonResponse(tarea_serializer.data,safe=False)
    elif request.method == 'POST':
        tarea_data = JSONParser().parse(request)
        tarea_serializer = TareasSerializer(data=tarea_data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
            return JsonResponse("Agregado correctamente",safe=False)
        return JsonResponse("Fallo al agregar",safe=False)

