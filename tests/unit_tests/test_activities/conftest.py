import pytest

from activities.models import Activity


@pytest.fixture
def activity(db, user):
    return Activity.objects.create(
        user=user,
        name="Hiking",
        nature="Relaxing and Involving",
        type="Outdoors",
    )


def activity1(db, user1):
    return Activity.objects.create(
        user=user1, name="Watching a movie", nature="Relaxing", type="Indoors"
    )
