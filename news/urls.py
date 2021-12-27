from rest_framework import routers
from .views import TagViewSet, NewsViewSet, SourceViewSet

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'sources', SourceViewSet)
router.register(r'news', NewsViewSet)
