from rest_framework import viewsets

from .models import *
from .serializers import *

class ProduitViewSet(viewsets.ModelViewSet):
	queryset = Produit.objects.all()
	serializer_class = ProduitSerializer

class AchatViewSet(viewsets.ModelViewSet):
	queryset = Achat.objects.all()
	serializer_class = AchatSerializer

class VenteViewSet(viewsets.ModelViewSet):
	queryset = Vente.objects.all()
	serializer_class = VenteSerializer
