from rest_framework import routers
from .views import FeaturesViewSet

router = routers.DefaultRouter()
router.register(r'features', FeaturesViewSet)
