import factory
from faker import Factory as FakerFactory
from pytest_factoryboy import register

from activities.models import Activity, Tag
from tests.unit_tests.test_accounts.factories import UserFactory

faker = FakerFactory.create()


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.lazy_attribute(lambda x: faker.word())
    user = factory.SubFactory(UserFactory)


class ActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Activity

    user = factory.SubFactory(UserFactory)
    name = factory.LazyAttribute(lambda x: faker.sentence(nb_words=3))
    nature = factory.LazyAttribute(lambda x: faker.sentence(nb_words=3))
    tag = factory.SubFactory(TagFactory)


register(TagFactory)
register(ActivityFactory)
