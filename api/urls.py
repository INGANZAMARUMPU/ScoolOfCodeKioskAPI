from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

router = routers.DefaultRouter()

router.register("produits", ProduitViewSet)
router.register("achats", AchatViewSet)
router.register("ventes",VenteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]
