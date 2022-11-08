from rest_framework import viewsets

from .models import *
from .serializers import *

class ProduitViewSet(viewsets.ModelViewSet):
	queryset = Produit.objects.all()
	serializer_class = ProduitSerializer

class AchatViewSet(viewsets.ModelViewSet):
	queryset = Achat.objects.all()
	serializer_class = AchatSerializer

	def perform_create(self, serializer):
		serializer.save(
			user = self.request.user
		)
	    

class VenteViewSet(viewsets.ModelViewSet):
	queryset = Vente.objects.all()
	serializer_class = VenteSerializer

	def perform_create(self, serializer):
		serializer.save(
			user = self.request.user,
			prix = serializer.validated_data["quantite"] * serializer.validated_data["produit"].prix_vente
		)
