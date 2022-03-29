from rest_framework.test import APIClient

import pytest


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture
def user(db, django_user_model, django_username_field):
    UserModel = django_user_model
    username_field = django_username_field

    try:
        user = UserModel._default_manager.get(**{username_field: "user@test.com"})
    except UserModel.DoesNotExist:
        user = UserModel._default_manager.create_user(
            "user@test.com", "Test", "User", "testpass123"
        )
    return user


@pytest.fixture
def user1(db, django_user_model, django_username_field):
    UserModel = django_user_model
    username_field = django_username_field

    try:
        user = UserModel._default_manager.get(**{username_field: "user1@test.com"})
    except UserModel.DoesNotExist:
        user = UserModel._default_manager.create_user(
            "user1@test.com", "Test", "User1", "testpass123"
        )
    return user


@pytest.fixture
def admin_user(db, django_user_model, django_username_field):
    UserModel = django_user_model
    username_field = django_username_field

    try:
        user = UserModel._default_manager.get(**{username_field: "admin@test.com"})
    except UserModel.DoesNotExist:
        user = UserModel._default_manager.create_superuser(
            "admin@test.com", "Test", "Admin", "password"
        )
    return user


@pytest.fixture
def client():
    """Client for an unauthenticated user."""
    client = APIClient()
    return client


@pytest.fixture
def user_client(db, client, user):
    client.force_login(user)
    return client


@pytest.fixture
def user1_client(db, client, user1):
    client.force_login(user1)
    return client


@pytest.fixture
def admin_client(db, client, admin_user):
    client.force_login(admin_client)
    return client
