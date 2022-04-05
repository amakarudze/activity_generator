import pytest

from activities.models import Activity, Tag


@pytest.fixture
def tag(db, user):
    return Tag.objects.create(user=user, name="Outdoor")


@pytest.fixture
def activity(db, user, tag):
    return Activity.objects.create(
        user=user,
        name="Hiking",
        nature="Relaxing and Involving",
        tag=tag,
    )


@pytest.fixture
def activity1(db, user1):
    return Activity.objects.create(
        user=user1, name="Watching a movie", nature="Relaxing", type="Indoors"
    )


@pytest.fixture
def tag2(db, user):
    return Tag.objects.create(user=user, name="Indoor")


@pytest.fixture
def tag3(db, user1):
    return Tag.objects.create(user=user1, name="Workout")


@pytest.fixture
def tag_invalid(user):
    payload = {"user": user, "name": ""}
    return payload


@pytest.fixture
def create_tag(user):
    payload = {"user": user, "name": "Skills"}
    return payload


@pytest.fixture
def activity(db, user, tag):
    return Activity.objects.create(user=user, name="Hiking", nature="Physical", tag=tag)


@pytest.fixture
def activity2(db, user, tag):
    return Activity.objects.create(
        user=user, name="Baking", nature="Household Chores", tag=tag
    )


@pytest.fixture
def activity3(db, user1, tag3):
    return Activity.objects.create(
        user=user1, name="Brisk Walking", nature="Exercising", tag=tag3
    )


@pytest.fixture
def create_activity(user, tag):
    payload = {
        "user": user.pk,
        "name": "Walking",
        "nature": "Exercising",
        "tag": tag.pk,
    }
    return payload


@pytest.fixture
def partial_update(tag2):
    payload = {"name": "Watching a movie", "tag": tag2.pk}
    return payload


@pytest.fixture
def full_update(tag2):
    payload = {"name": "Watching a movie", "nature": "Relaxing", "tag": tag2.pk}
    return payload
