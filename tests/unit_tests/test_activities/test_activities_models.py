import pytest

from activities.models import Activity, Tag


@pytest.mark.unit
def test_activity_model_string_representation(activity, user):
    user_activity = Activity.objects.filter(user=user, name=activity.name).first()
    assert str(user_activity) == f"{user.email} - {activity.name}"


@pytest.mark.unit
def test_tag_model_string_representation(tag, user):
    new_tag = Tag.objects.filter(name=tag.name, user=user).first()
    assert str(new_tag) == tag.name
