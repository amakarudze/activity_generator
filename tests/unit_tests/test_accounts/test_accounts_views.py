from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status

CREATE_USER_URL = reverse("accounts:create")
TOKEN_URL = reverse("accounts:token")
ME_URL = reverse("accounts:me")


def test_create_user_success(user2, client):
    """Test create user with valid payload."""
    payload = user2
    response = client.post(CREATE_USER_URL, payload)
    assert response.status_code == status.HTTP_201_CREATED
    user = get_user_model().objects.get(**response.data)
    assert user.check_password(payload["password"])


def test_user_exists(client, user, user3):
    """Test create a user that already exists fails."""
    payload = user3
    response = client.post(CREATE_USER_URL, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_password_too_short(client, user4):
    payload = user4
    response = client.post(CREATE_USER_URL, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    user_exists = get_user_model().objects.filter(email=payload["email"]).exists()
    assert user_exists is False


def test_create_token_for_user(client, user, create_token):
    payload = create_token
    response = client.post(TOKEN_URL, payload)
    assert "token" in response.data
    assert response.status_code == status.HTTP_200_OK


def test_create_token_invalid_credentials(client, user, token_invalid_credentials):
    payload = token_invalid_credentials
    response = client.post(TOKEN_URL, payload)
    assert "token" not in response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_token_no_user(client, token_no_user):
    payload = token_no_user
    response = client.post(TOKEN_URL, payload)
    assert "token" not in response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_token_missing_field(client, user, token_missing_field):
    payload = token_missing_field
    response = client.post(TOKEN_URL, payload)
    assert "token" not in response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_retrieve_user_unauthorized(client):
    response = client.get(ME_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
