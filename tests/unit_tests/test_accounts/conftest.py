from django.contrib.auth import get_user_model

import pytest


def create_user(**params):
    return get_user_model().objects.create_user(**params)


@pytest.fixture
def user2():
    payload = {
        "email": "testuser@test.com",
        "first_name": "Test",
        "last_name": "User2",
        "password": "Pass1234D",
    }
    return payload


@pytest.fixture
def user3():
    payload = {
        "email": "user@test.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "Pass1234D",
    }
    return payload


@pytest.fixture
def user4():
    payload = {
        "email": "test@test.com",
        "first_name": "Test",
        "last_name": "User4",
        "password": "Pass",
    }
    return payload
