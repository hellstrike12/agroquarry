from django_filters import rest_framework
from django import forms
from main.models import Soja, Milho, Cafe
from main.serializers import SojaSerializer, MilhoSerializer, CafeSerializer
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Filtros
class SojaFilter(rest_framework.FilterSet):
    data_inicio = rest_framework.DateFilter('data', 'gte', label='Data Inicial')
    data_fim = rest_framework.DateFilter('data', 'lte', label='Data Final')
    class Meta:
        model = Soja
        fields = []

class MilhoFilter(rest_framework.FilterSet):
    data_inicio = rest_framework.DateFilter('data', 'gte', label='Data Inicial')
    data_fim = rest_framework.DateFilter('data', 'lte', label='Data Final')
    class Meta:
        model = Milho
        fields = []

class CafeFilter(rest_framework.FilterSet):
    data_inicio = rest_framework.DateFilter('data', 'gte', label='Data Inicial')
    data_fim = rest_framework.DateFilter('data', 'lte', label='Data Final')
    class Meta:
        model = Cafe
        fields = []

# Páginas
class SojaList(generics.ListCreateAPIView):
    """
    Listar todas as cotações de soja ou criar uma nova
    """

    queryset = Soja.objects.all()
    serializer_class = SojaSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = SojaFilter

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
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = MilhoFilter

class MilhoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhar, atualizar ou excluir uma cotação de milho específica
    """

    queryset = Milho.objects.all()
    serializer_class = MilhoSerializer

# Todas as cotações de café
class CafeList(generics.ListCreateAPIView):
    """
    Listar todas as cotações de café ou criar uma nova
    """

    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = CafeFilter

class CafeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhar, atualizar ou excluir uma cotação de café específica
    """

    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

# Somente café arabica
class CafeArabicaList(generics.ListAPIView):
    """
    Listar todas as cotações do café arábica
    """
    queryset = Cafe.objects.filter(tipo__exact="Arabica")
    serializer_class = CafeSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = CafeFilter

# Somente café conillon
class CafeConillonList(generics.ListAPIView):
    """
    Listar todas as cotações do café conillon
    """
    queryset = Cafe.objects.filter(tipo__exact="Conillon")
    serializer_class = CafeSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = CafeFilter