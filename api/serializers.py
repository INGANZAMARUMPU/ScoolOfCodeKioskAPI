from rest_framework import serializers
from .models import *

class ProduitSerializer(serializers.ModelSerializer):

	class Meta:
		model = Produit
		fields = "__all__"

	def to_representation(self, obj):
		serializer = super().to_representation(obj)

		## calcule quantite, total_achats, total_ventes
		# achats = Achat.objects.filter(produit=obj)
		# qtt_achat = 0
		# prix_achat = 0
		# for achat in achats:
		# 	qtt_achat += achat.quantite
		# 	prix_achat += achat.prix_total

		# ventes = Vente.objects.filter(produit=obj)
		# qtt_vente = 0
		# prix_vente = 0
		# for vente in ventes:
		# 	qtt_vente += vente.quantite
		# 	prix_vente += vente.prix

		# django Version of totals computation
		qtt_achat = Achat.objects.filter(produit=obj).aggregate(
			models.Sum('quantite')
		)["quantite__sum"] or 0

		prix_achat = Achat.objects.filter(produit=obj).aggregate(
			models.Sum('prix_total')
		)["prix_total__sum"] or 0

		qtt_vente = Vente.objects.filter(produit=obj).aggregate(
			models.Sum('quantite')
		)["quantite__sum"] or 0

		prix_vente = Vente.objects.filter(produit=obj).aggregate(
			models.Sum('prix')
		)["prix__sum"] or 0

		serializer["quantite"] = qtt_achat - qtt_vente
		serializer["total_achats"] = prix_achat
		serializer["total_ventes"] = prix_vente

		return serializer

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
