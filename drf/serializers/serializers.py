from rest_framework import serializers
from .models import Quotes


class QuotesSerializer(serializers.Serializer):
    text=serializers.CharField()

    def create(self,validate_data):
        return Quotes.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.text=validated_data.get('text',instance.text)
        instance.save()
        return instance
    
    