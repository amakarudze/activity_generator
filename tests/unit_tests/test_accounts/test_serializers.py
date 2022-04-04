import factory
import pytest

from accounts.serializers import UserSerializer, AuthTokenSerializer
from tests.unit_tests.test_accounts.factories import UserFactory, TokenFactory


@pytest.mark.unit
def test_serialize_user_model():
    user = UserFactory()
    serializer = UserSerializer(user)

    assert serializer.data


@pytest.mark.unit
def test_serialized_data(mocker):
    valid_serialized_data = factory.build(dict, FACTORY_CLASS=UserFactory)

    serializer = UserSerializer(data=valid_serialized_data)
    assert serializer.is_valid()
    assert serializer.errors == {}


@pytest.mark.unit
def test_serialize_token():
    token = TokenFactory()
    serializer = AuthTokenSerializer(token)

    assert serializer.data
