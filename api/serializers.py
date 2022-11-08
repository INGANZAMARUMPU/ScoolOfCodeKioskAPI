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

	def to_representation(self, obj):
		serializer = super().to_representation(obj)
		serializer["user"] = obj.user.username
		serializer["produit"] = str(obj.produit)
		return serializer

class VenteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vente
		exclude = ["user", "prix"]

	def to_representation(self, obj):
		serializer = super().to_representation(obj)
		serializer["user"] = obj.user.username
		serializer["produit"] = str(obj.produit)
		serializer["prix"] = obj.prix
		return serializer
