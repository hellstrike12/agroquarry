from main.models import Soja, Milho, Cafe
from main.serializers import SojaSerializer, MilhoSerializer, CafeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class SojaList(APIView):
    """
    Listar todas as cotações de soja ou criar uma nova
    """

    def get(self, request, format=None):
        soja = Soja.objects.all()
        serializer = SojaSerializer(soja, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SojaSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SojaDetail(APIView):
    """
    Detalhar, atualizar ou excluir uma cotação de soja específica
    """

    def get_object(self, pk):
        try:
            return Soja.objects.get(pk=pk)
        except Soja.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        soja = self.get_object(pk)
        serializer = SojaSerializer(soja)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        soja = self.get_object(pk)
        serializer = SojaSerializer(soja, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        soja = self.get_object(pk)
        soja.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MilhoList(APIView):
    """
    Listar todas as cotações de milho ou criar uma nova
    """

    def get(self, request, format=None):
        milho = Milho.objects.all()
        serializer = MilhoSerializer(milho, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MilhoSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MilhoDetail(APIView):
    """
    Detalhar, atualizar ou excluir uma cotação de milho específica
    """

    def get_object(self, pk):
        try:
            return Milho.objects.get(pk=pk)
        except Milho.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        milho = self.get_object(pk)
        serializer = MilhoSerializer(milho)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        milho = self.get_object(pk)
        serializer = MilhoSerializer(milho, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        milho = self.get_object(pk)
        milho.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CafeList(APIView):
    """
    Listar todas as cotações de café ou criar uma nova
    """

    def get(self, request, format=None):
        cafe = Cafe.objects.all()
        serializer = CafeSerializer(cafe, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CafeSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CafeDetail(APIView):
    """
    Detalhar, atualizar ou excluir uma cotação de café específica
    """

    def get_object(self, pk):
        try:
            return Cafe.objects.get(pk=pk)
        except Cafe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cafe = self.get_object(pk)
        serializer = CafeSerializer(cafe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cafe = self.get_object(pk)
        serializer = CafeSerializer(cafe, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cafe = self.get_object(pk)
        cafe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
