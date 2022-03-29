from django.contrib.auth import get_user_model

import pytest


def create_user(**params):
    return get_user_model().objects.create_user(**params)


@pytest.fixture
def user2():
    payload = {
      'email': 'testuser@test.com',
      'password': 'Pass1234D',
      'name': 'Test User2'
    }
    return payload


@pytest.fixture
def user3():
    payload = {
      'email': 'user@test.com',
      'password': 'Pass1234D',
      'name': 'Test User'
    }
    return payload


@pytest.fixture
def user4():
    payload = {
      'email': 'test@test.com',
      'password': 'Pass',
      'name': 'Test User'
    }
    return payload