from rest_framework import serializers
from main.models import Soja, Milho, Cafe, CAFE_CHOICES

# Crie seus serializadores aqui


class SojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soja
        fields = ['id', 'data', 'cotacao', 'variacao']


class MilhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milho
        fields = ['id', 'data', 'cotacao', 'variacao']

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['id', 'tipo', 'data', 'cotacao', 'variacao']
