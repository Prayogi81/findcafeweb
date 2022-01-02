from rest_framework.routers import DefaultRouter
from .viewset_api import CafeViewset
from django.urls import path, include

router =  DefaultRouter()
router.register('cafe', CafeViewset)


urlpatterns = [
    path('api/', include(router.urls)),
]