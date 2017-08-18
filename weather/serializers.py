from rest_framework import serializers
from weather.models import Light


class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = '__all__'
        