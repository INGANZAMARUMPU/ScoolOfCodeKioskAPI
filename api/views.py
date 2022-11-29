from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *

class TokenPairView(TokenObtainPairView):
    serializer_class = TokenPairSerializer

class ProduitViewSet(viewsets.ModelViewSet):
	queryset = Produit.objects.all()
	serializer_class = ProduitSerializer
	filter_backends = [filters.DjangoFilterBackend, ]
	filterset_fields = {
		'prix_vente': ['gte', 'lte'],
		'nom': ['icontains',],
	}

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
	filter_backends = [filters.DjangoFilterBackend, ]
	filterset_fields = {
		'produit': ['exact']
	}

	def perform_create(self, serializer):
		prix_vente = serializer.validated_data["produit"].prix_vente
		quantite = serializer.validated_data["quantite"]
		serializer.save(
			user = self.request.user,
			prix =  quantite*prix_vente
		)
