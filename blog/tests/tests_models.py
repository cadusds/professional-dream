from django.contrib.auth import get_user_model
from django.test import TestCase
from blog.models import Profile, Tag


class TestProfile(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        get_user_model().objects.create()

    def test_create_profile(self):
        user = get_user_model().objects.last()
        profile = Profile.objects.create(user=user)
        self.assertEqual(profile.user.pk, user.pk)
        self.assertEqual(profile.__str__(), "")


class TestTag(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Tag.objects.create(name="tag-test")

    def test_str_attributes(self):
        self.assertEqual(Tag.objects.last().__str__(), 'tag-test')
