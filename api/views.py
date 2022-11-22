from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters

from .models import *
from .serializers import *

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

class CommuneViewSet(viewsets.GenericViewSet):

	def list(self, request):
		return Response({
			"BUBANZA":{
				"Bubanza":[],
				"Bubanza":[],
				"Gihanga":[],
				"Musigati":[],
				"Mpanda":[],
				"Rugazi":[]
			},
			"BUJUMBURA MAIRIE":{
				"Mukaza":[ "Buyenzi", "Bwiza", "Nyakabiga", "Rohero"],
				"Ntahangwa":[ "Cibitoke", "Kamenge", "Kinama", "Ngagara", "Gihosha", "Buterere"],
				"Muha":["Musaga", "Kinindo", "Kanyosha"]
			},
			"BUJUMBURA":{
				"Isale":[],
				"Kabezi":[],
				"Kanyosha":[], 
				"Mubimbi":[],
				"Mugongomanga":[],
				"Mukike":[],
				"Mutimbuzi":[],
				"Nyabiraba":[]
			},
			"BURURI":{
				"Matana": [],
				"Bururi": [],
				"Mugamba": [],
				"Rutovu": [],
				"Songa": [],
				"Vyanda": []
			},
			"RUMONGE":{
				"Bugarama":[],
				"Burambi":[],
				"Buyengero":[],
				"Muhuta":[],
				"Rumonge":[]
			},
			"CANKUZO":{
				"Cankuzo":[],
				"Cendajuru":[],
				"Gisagara":[],
				"Kigamba":[],
				"Mishiha":[]
			},
			"CIBITOKE":{
				"Buganda": [],
				"Bukinanyana": [],
				"Mabayi": [],
				"Mugina": [],
				"Murwi": [],
				"Rugombo": []
			},
			"GITEGA":{
				"Bugendana":[],
				"Bukirasazi":[],
				"Buraza":[],
				"Giheta":[],
				"Gishubi":[],
				"Gitega":[],
				"Itaba":[],
				"Makebuko":[],
				"Mutaho":[],
				"Nyarusange":[],
				"Ryansoro":[], 
			},
			"KARUZI":{
				"Bugenyuzi":[],
				"Buhiga":[],
				"Gihogazi":[],
				"Gitaramuka":[],
				"Mutumba":[],
				"Nyabikere":[],
				"Shombo":[]
			},
			"KAYANZA":{
				"Butaganzwa":[],
				"Gahombo":[],
				"Gatara":[],
				"Kabarore":[],
				"Kayanza":[],
				"Matongo":[],
				"Muhanga":[],
				"Muruta":[],
				"Rango":[]
			},
			"KIRUNDO":{
				"Bugabira": [],
				"Busoni": [],
				"Bwambarangwe": [],
				"Gitobe": [],
				"Kirundo": [],
				"Ntega": [],
				"Vumbi": []
			},
			"MAKAMBA":{
				"Kayogoro": [],
				"Kibago": [],
				"Mabanda": [],
				"Makamba": [],
				"Nyanza-Lac": [],
				"Vugizo": []
			},
			"MURAMVYA":{
				"Bukeye": [],
				"Kiganda": [],
				"Mbuye": [],
				"Muramvya": [],
				"Rutegama": []
			},
			"MUYINGA":{
				"Buhinyuza": [],
				"Butihinda": [],
				"Gashoho": [],
				"Gasorwe": [],
				"Giteranyi": [],
				"Muyinga": [],
				"Mwakiro": []
			},
			"MWARO":{
				"Bisoro": [],
				"Gisozi": [],
				"Kayokwe": [],
				"Ndava": [],
				"Nyabihanga": [],
				"Rusaka": []
			},
			"NGOZI":{
				"Busiga":[],
				"Gashikanwa":[],
				"Kiremba":[],
				"Marangara":[],
				"Mwumba":[],
				"Ngozi":[],
				"Nyamurenza":[],
				"Ruhororo":[],
				"Tangara":[]
			},
			"RUTANA":{
				"Bukemba": [],
				"Giharo": [],
				"Gitanga": [],
				"Mpinga-Kayove": [],
				"Musongati": [],
				"Rutana": []
			},
			"RUYIGI":{
				"Butaganzwa": [],
				"Butezi": [],
				"Bweru": [],
				"Gisuru": [],
				"Kinyinya": [],
				"Nyabitsinda": [],
				"Ruyigi": []
			}
		}, 200)