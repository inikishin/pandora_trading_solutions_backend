from rest_framework import routers
from .views import MLModelViewSet, HorizonViewSet, PredictionViewSet, FitResultsViewSet

router = routers.DefaultRouter()
router.register(r'ml-models', MLModelViewSet)
router.register(r'horizons', HorizonViewSet)
router.register(r'predictions', PredictionViewSet)
router.register(r'fit-results', FitResultsViewSet)
