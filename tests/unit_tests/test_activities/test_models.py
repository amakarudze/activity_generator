import pytest

from activities.models import Activity


@pytest.mark.unit
def test_string_representation(activity, user):
    user_activity = Activity.objects.filter(user=user, name=activity.name).first()
    assert str(user_activity) == f"{user.get_full_name()} - {activity.name}"
