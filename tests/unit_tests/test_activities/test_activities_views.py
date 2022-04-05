from genericpath import exists
from urllib import response
from django.urls import reverse

import pytest
from rest_framework import status

from activities.models import Activity, Tag
from activities.serializers import ActivitySerializer, TagSerializer


TAGS_URL = reverse("activities:tag-list")
ACTIVITIES_URL = reverse("activities:activity-list")


def detail_url(activity_id):
    return reverse("activities:activity-detail", args=[activity_id])


@pytest.mark.unit
def test_access_tags_unauthenticated(client):
    response = client.get(TAGS_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.unit
def test_access_tags(user_client, tag, tag2):
    response = user_client.get(TAGS_URL)

    tags = Tag.objects.all().order_by("-name")
    serializer = TagSerializer(tags, many=True)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data


@pytest.mark.unit
def test_tags_limited_user(user_client, tag, tag3):
    response = user_client.get(TAGS_URL)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == tag.name


@pytest.mark.unit
def test_create_tag_successfully(user_client, user, create_tag):
    payload = create_tag
    user_client.post(TAGS_URL, payload)
    exists = Tag.objects.filter(user=user, name=payload["name"]).exists()
    assert exists


@pytest.mark.unit
def test_create_tag_invalid(user_client, tag_invalid):
    payload = tag_invalid
    response = user_client.post(TAGS_URL, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.unit
def test_retrieve_tags_assigned_to_activities(user_client, tag, tag2, activity):
    response = user_client.get(TAGS_URL, {"assigned_only": 1})
    serializer1 = TagSerializer(tag)
    serializer2 = TagSerializer(tag2)

    assert serializer1.data in response.data
    assert serializer2.data not in response.data


@pytest.mark.unit
def test_retrieve_tags_assigned_unique(user_client, tag, tag2, activity, activity2):
    response = user_client.get(TAGS_URL, {"assigned_only": 1})
    assert len(response.data) == 1


@pytest.mark.unit
def test_activities_auth_required(client):
    response = client.get(ACTIVITIES_URL)
    response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.unit
def test_retrieve_activities(activity, activity2, user_client):
    response = user_client.get(ACTIVITIES_URL)

    activities = Activity.objects.all().order_by("-id")
    serializer = ActivitySerializer(activities, many=True)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data


@pytest.mark.unit
def test_activities_limited_to_user(activity, activity2, activity3, user, user_client):
    response = user_client.get(ACTIVITIES_URL)

    activities = Activity.objects.filter(user=user).order_by("-id")
    serializer = ActivitySerializer(activities, many=True)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data


@pytest.mark.unit
def test_view_activity_detail(user_client, activity2):
    url = detail_url(activity2.id)

    response = user_client.get(url)
    serializer = ActivitySerializer(activity2)
    assert response.data == serializer.data


@pytest.mark.unit
def test_create_activity(create_activity, user, user_client):
    payload = create_activity
    response = user_client.post(ACTIVITIES_URL, payload)

    assert response.status_code == status.HTTP_201_CREATED
    exists = Activity.objects.filter(user=user, name=payload["name"]).exists()
    assert exists


@pytest.mark.unit
def test_partial_update_activity(activity2, partial_update, user_client):
    payload = partial_update
    url = detail_url(activity2.id)
    response = user_client.patch(url, payload)

    activity2.refresh_from_db()
    assert activity2.name == payload["name"]
    assert activity2.tag.pk == payload["tag"]
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.unit
def test_full_update_activity(activity2, full_update, user_client):
    payload = full_update
    url = detail_url(activity2.id)
    response = user_client.patch(url, payload)

    activity2.refresh_from_db()
    assert activity2.name == payload["name"]
    assert activity2.tag.pk == payload["tag"]
    assert activity2.nature == payload["nature"]
    assert response.status_code == status.HTTP_200_OK
