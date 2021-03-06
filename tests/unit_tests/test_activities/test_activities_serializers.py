import pytest

from activities.serializers import ActivitySerializer, TagSerializer
from tests.unit_tests.test_activities.factories import ActivityFactory, TagFactory


@pytest.mark.unit
def test_serialize_activity_model():
    activity = ActivityFactory()
    serializer = ActivitySerializer(activity)

    assert serializer.data


@pytest.mark.unit
def test_activity_serialized_data(user, tag):
    t = ActivityFactory.build()
    valid_serialized_data = {
        "user": user.pk,
        "name": t.name,
        "nature": t.nature,
        "tag": tag.pk,
    }
    serializer = ActivitySerializer(data=valid_serialized_data)

    assert serializer.is_valid(raise_exception=True)
    assert serializer.errors == {}


@pytest.mark.unit
def test_tag_serializer():
    tag = TagFactory()
    serializer = TagSerializer(tag)

    assert serializer.data


@pytest.mark.unit
def test_tag_serializer_data(mocker):
    t = TagFactory.build()
    valid_serializer_data = {"user": t.user.pk, "name": t.name}

    serializer = TagSerializer(data=valid_serializer_data)

    assert serializer.is_valid(raise_exception=True)
    assert serializer.errors == {}
