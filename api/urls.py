from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register("produits", ProduitViewSet)
router.register("achats", AchatViewSet)
router.register("ventes",VenteViewSet)
router.register("communes", CommuneViewSet, basename="communes")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]