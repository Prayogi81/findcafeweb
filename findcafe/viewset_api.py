from findcafe.models import Cafe
from findcafe.serializers import CafeSerializer
from rest_framework import serializers, viewsets

class CafeViewset(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer