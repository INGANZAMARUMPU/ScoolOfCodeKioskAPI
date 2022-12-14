from django.db import models
from django.contrib.auth.models import User

class Produit(models.Model):
	id = models.AutoField(primary_key=True)
	nom = models.CharField(max_length=64, unique=True)
	prix_vente = models.IntegerField()

	def __str__(self):
		return f"{self.nom} de {self.prix_vente}FBu"

class Achat(models.Model):
	id = models.BigAutoField(primary_key=True)
	produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
	quantite = models.IntegerField()
	prix_total = models.IntegerField()
	date = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.quantite} {self.produit.nom}s coutant {self.prix_total}FBu"

class Vente(models.Model):
	id = models.BigAutoField(primary_key=True)
	produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
	quantite = models.IntegerField()
	prix = models.IntegerField()
	date = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.quantite} {self.produit.nom} à {self.prix_total}FBu"