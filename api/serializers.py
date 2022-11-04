from rest_framework import serializers
from .models import *

class ProduitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Produit
		fields = "__all__"

class AchatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Achat
		exclude = ["user"]

class VenteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vente
		exclude = ["user"]
