from django.http import JsonResponse

#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from beautypal.models import Room
#from beautypal.serializers import RoomSerializer
#from beautypal.api import serializers

#@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return JsonResponse(routes, safe=False)