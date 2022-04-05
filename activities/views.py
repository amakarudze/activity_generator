from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Activity, Tag
from .serializers import ActivitySerializer, TagSerializer


class TagViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """Viewset for Tag objects."""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        assigned_only = bool(int(self.request.query_params.get("assigned_only", 0)))
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(activity__isnull=False)

        return queryset.filter(user=self.request.user).order_by("-name").distinct()

    def perform_create(self, serializer):
        """Create a new tag"""
        serializer.save(user=self.request.user)


class ActivityViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    """Manage activities in the database."""

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(user=self.request.user).order_by("-id")

    def perform_create(self, serializer):
        """Create a new activity."""
        serializer.save(user=self.request.user)
