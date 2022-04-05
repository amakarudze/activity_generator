from rest_framework import serializers

from activities.models import Activity, Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects."""

    class Meta:
        model = Tag
        fields = ("id", "name")
        read_only_fields = ("id",)


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for the activity model."""

    class Meta:
        model = Activity
        fields = ("id", "user", "name", "nature", "tag")
        read_only_fields = ("id",)
