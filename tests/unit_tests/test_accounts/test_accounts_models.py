from django.contrib.auth import get_user_model
from django.forms import ValidationError

import pytest


@pytest.mark.unit
def test_user_string_representation(test_user):
    assert str(test_user) == "user@test.com"


@pytest.mark.unit
def test_user_get_full_name(test_user):
    assert test_user.get_full_name() == "Test User"


@pytest.mark.unit
def test_user_get_short_name(test_user):
    assert test_user.get_short_name() == "Test"


@pytest.mark.unit
def test_create_user_object_fails_without_email(db):
    with pytest.raises(ValidationError):
        get_user_model().objects.create_user(None, "First", "Last", "Testpass125")
