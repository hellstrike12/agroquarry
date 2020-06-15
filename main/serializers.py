from rest_framework import serializers
from main.models import Soja, Milho, Cafe, CAFE_CHOICES

# Crie seus serializadores aqui


class SojaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    data = serializers.DateField()
    cotacao = serializers.FloatField()
    variacao = serializers.FloatField()


class MilhoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    data = serializers.DateField()
    cotacao = serializers.FloatField()
    variacao = serializers.FloatField()


class CafeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tipo = serializers.ChoiceField(choices=CAFE_CHOICES, default='Arabica')
    data = serializers.DateField()
    cotacao = serializers.FloatField()
    variacao = serializers.FloatField()
