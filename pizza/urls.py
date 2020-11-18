from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToppingsViewSet, PizzaViewSet

#Code from here

app_name = "pizza"
router = DefaultRouter()
router.register(r'allpizza',PizzaViewSet,basename="allpizza")
router.register(r'toppings',ToppingsViewSet,basename="toppings")

urlpatterns = [
    path('',include(router.urls))
]
