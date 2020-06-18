from main.models import Soja, Milho, Cafe
from main.serializers import SojaSerializer, MilhoSerializer, CafeSerializer
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
class SojaList(generics.ListCreateAPIView):
    """
    Listar todas as cotações de soja ou criar uma nova
    """

    queryset = Soja.objects.all()
    serializer_class = SojaSerializer

@csrf_exempt
class SojaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhar, atualizar ou excluir uma cotação de soja específica
    """

    queryset = Soja.objects.all()
    serializer_class = SojaSerializer

@csrf_exempt
class MilhoList(generics.ListCreateAPIView):
    """
    Listar todas as cotações de milho ou criar uma nova
    """

    queryset = Milho.objects.all()
    serializer_class = MilhoSerializer

@csrf_exempt
class MilhoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhar, atualizar ou excluir uma cotação de milho específica
    """

    queryset = Milho.objects.all()
    serializer_class = MilhoSerializer

@csrf_exempt
class CafeList(generics.ListCreateAPIView):
    """
    Listar todas as cotações de café ou criar uma nova
    """

    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

@csrf_exempt
class CafeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhar, atualizar ou excluir uma cotação de café específica
    """

    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer