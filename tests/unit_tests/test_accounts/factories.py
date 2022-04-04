import factory
from faker import Factory as FakerFactory
from pytest_factoryboy import register

from accounts.models import User

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    email = factory.LazyAttribute(lambda x: faker.email())
    password = factory.LazyAttribute(lambda x: faker.password())


class TokenFactory(factory.Factory):
    class Meta:
        model = User

    email = factory.LazyAttribute(lambda x: faker.email())
    password = factory.LazyAttribute(lambda x: faker.password())


register(UserFactory)
register(TokenFactory)
