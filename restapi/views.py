from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from bankapp.models import Indianbank
from .serializers import IndianbankSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class IndianbankAPIView(APIView):

    def get(self, request):
        Indianbanks = Indianbank.objects.all()
        serializer = IndianbankSerializer(Indianbanks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IndianbankSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndianbankDetails(APIView):
    def get_object(self, id):
        try:
            return Indianbank.objects.get(id=id)

        except Indianbank.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_NOT_FOUND)    
        

    def get(self, request, id):
        indianbank = self.get_object(id)
        serializer = IndianbankSerializer(indianbank)
        return Response(serializer.data)

    def put(self, request, id):
        indianbank = self.get_object(id)
        serializer = IndianbankSerializer(indianbank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       
    def delete(self, request, id):
        indianbank = self.get_object(id)
        indianbank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
