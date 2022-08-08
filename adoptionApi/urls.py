from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.AnimalViewSet)
router.register(r'animal', views.AnimalViewSet)
 
urlpatterns = [
    path('api', include(router.urls)), 
]
    
