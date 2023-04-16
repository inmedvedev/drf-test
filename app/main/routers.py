from rest_framework import routers
from entity.viewset import EntityViewSet

router = routers.DefaultRouter()
router.register(r"entities", EntityViewSet, basename="entities")
