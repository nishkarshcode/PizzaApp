from rest_framework import serializers
from .models import Toppings, Pizza

#code from here

class ToppingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Toppings
        fields = ['id','name','updated_at','created_at']
        read_only_fields = ['id',]
    
    def to_representation(self, value):
        return value.name


class PizzaSerializer(serializers.ModelSerializer):
    toppings = ToppingsSerializer(many=True)
    
    class Meta:
        model = Pizza
        fields = ['id','name','pizza_type','toppings','sizes','updated_at','created_at']
