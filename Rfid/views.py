from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Rfid
from .serializers import RfidSerializer

class RfidView(APIView):

    def get(self, request, format=None):
        queryset = Rfid.objects.all()
        serializer = RfidSerializer(queryset, many=True, context = {'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RfidSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response (datas, status=status.HTTP_200_OK)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

class RfidDetail(APIView):
    def get_object(self,pk):
        try: 
            return Rfid.objects.get(pk=pk)
        except Rfid.DoesNotExist:
            raise Http404
    def get(self, request,pk, format=None):
        rfid = self.get_object(pk) 
        serializer = RfidSerializer(rfid)
        return Response(serializer.data) 
    def put(self, request,pk, format=None):
        rfid = self.get_object(pk)
        serializer = RfidSerializer(rfid, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        rfid = self.get_object(pk)
        rfid.delete()
        return Response('Eliminado')


class RfidDetailNumberRFID(APIView):
    def get_object(self,number_rfid):
        try: 
            return Rfid.objects.get(number_rfid=number_rfid)
        except Rfid.DoesNotExist:
            raise Http404
    def get(self, request,number_rfid, format=None):
        rfid = self.get_object(number_rfid) 
        serializer = RfidSerializer(rfid)
        return Response(serializer.data) 
    # def put(self, request,pk, format=None):
    #     rfid = self.get_object(pk)
    #     serializer = RfidSerializer(rfid, data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def delete(self, request, pk, format=None):
    #     rfid = self.get_object(pk)
    #     rfid.delete()
    #     return Response('Eliminado')