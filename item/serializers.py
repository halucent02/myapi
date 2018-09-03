from rest_framework import serializers
from .models import Item
import os


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Item
        fields = ('id','name', 'file')
        read_only_fields = ('size',)
    
    def validate(self, validated_data):
            validated_data['size'] = validated_data['file'].size
            return validated_data

    def create(self, validated_data):
        return Item.objects.create(**validated_data)