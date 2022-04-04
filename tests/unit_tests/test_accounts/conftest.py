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


@pytest.fixture
def create_token():
    payload = {"email": "user@test.com", "password": "testpass123"}
    return payload


@pytest.fixture
def token_invalid_credentials():
    payload = {"email": "user@test.com", "password": "Testpass123"}
    return payload


@pytest.fixture
def token_no_user():
    payload = {"email": "test@test.com", "password": "pass1234"}
    return payload


@pytest.fixture
def token_missing_field():
    payload = {"email": "user@test.com", "password": ""}
    return payload


@pytest.fixture
def test_user(db, user3):
    return create_user(**user3)


@pytest.fixture
def update_user():
    payload = {"first_name": "Jane", "last_name": "Doe", "password": "Test#1234"}
    return payload
