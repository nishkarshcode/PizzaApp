from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Toppings, Pizza
from .serializers import ToppingsSerializer, PizzaSerializer
# Create your views here.

class ToppingsViewSet(viewsets.ModelViewSet):
    """Handle the create, update and delete functionality of the topping model"""
    queryset = Toppings.objects.all().order_by('-id')
    serializer_class = ToppingsSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    """Handle all create update and delete funtionality of Pizza model"""
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def _params_filter(self,qs):
        return [ para for para in qs.split(",")]

    def get_queryset(self):
        """ Return All the Pizza and You and filter that on url parameters"""
        queryset = self.queryset
        sizes = self.request.query_params.get('sizes', None)
        type1 = self.request.query_params.get('type', None)
        if sizes:
            allsizes = self._params_filter(sizes)
            queryset = queryset.filter(sizes__in=allsizes)
            print(queryset)
        if type1:
            alltype = self._params_filter(type1)
            queryset = queryset.filter(pizza_type__in=alltype)
        return queryset
    