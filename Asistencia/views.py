from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Asistencia
from .serializers import AsistenciaSerializer

class AsistenciaView(APIView):

    def get(self, request, format=None):
        queryset = Asistencia.objects.all()
        serializer = AsistenciaSerializer(queryset, many=True, context = {'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AsistenciaSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response (datas, status=status.HTTP_200_OK)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

class AsistenciaDetail(APIView):
    def get_object(self,pk):
        try: 
            return Asistencia.objects.get(pk=pk)
        except Asistencia.DoesNotExist:
            raise Http404
    def get(self, request,pk, format=None):
        asistencia = self.get_object(pk) 
        serializer = AsistenciaSerializer(asistencia)
        return Response(serializer.data) 
    def put(self, request,pk, format=None):
        asistencia = self.get_object(pk)
        serializer = AsistenciaSerializer(asistencia, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        asistencia = self.get_object(pk)
        asistencia.delete()
        return Response('Eliminado')