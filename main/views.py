from main.models import Soja, Milho, Cafe
from main.serializers import SojaSerializer, MilhoSerializer, CafeSerializer
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics

# Create your views here.
def index(request):
    return render(request, 'index.html')

class SojaList(generics.ListCreateAPIView):
    """
    Listar todas as cotações de soja ou criar uma nova
    """

    queryset = Soja.objects.all()
    serializer_class = SojaSerializer

class SojaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhar, atualizar ou excluir uma cotação de soja específica
    """

    queryset = Soja.objects.all()
    serializer_class = SojaSerializer

class MilhoList(generics.ListCreateAPIView):
    """
    Listar todas as cotações de milho ou criar uma nova
    """

    queryset = Milho.objects.all()
    serializer_class = MilhoSerializer

class MilhoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhar, atualizar ou excluir uma cotação de milho específica
    """

    queryset = Milho.objects.all()
    serializer_class = MilhoSerializer

class CafeList(generics.ListCreateAPIView):
    """
    Listar todas as cotações de café ou criar uma nova
    """

    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhar, atualizar ou excluir uma cotação de café específica
    """

    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer