from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated

from .models import Entity
from .serializers import EntityListSerializer, EntityCreateSerializer


class EntityViewSet(GenericViewSet, CreateModelMixin):
    queryset = Entity.objects.all().prefetch_related("properties")
    serializer_class = EntityListSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return EntityListSerializer
        if self.action == "create":
            return EntityCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)
