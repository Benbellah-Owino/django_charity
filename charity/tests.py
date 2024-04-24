# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Owner


class OwnerModelTestCase(TestCase):
    def setUp(self):
        self.owner = Owner.objects.create(
            email='testowner@example.com',
            username='testowner',
            phone='0754325543',
            gender='F',
            bank_account='0034 3423 9843 1246',
            bio='My name is a test owner'
        )

        # Create test groups
        self.group = Group.objects.create(name='Test Owner Group')

        # Create content type for owner model
        self.content_type = ContentType.objects.get_for_model(Owner)

        # Create test permission associated with owner model
        self.permission = Permission.objects.create(
            name='Test Owner Permission',
            codename='test_owner_permission',
            content_type=self.content_type
        )

    def test_owner_creation(self):
        # Test that a owner object is created successfully
        self.assertEqual(self.owner.email, 'testowner@example.com')
        self.assertEqual(self.owner.username, 'testowner')
        self.assertEqual(self.owner.phone, '0754325543')
        self.assertEqual(self.owner.gender, 'F')
        self.assertEqual(self.owner.bank_account, '0034 3423 9843 1246')
        self.assertEqual(self.owner.bio, 'My name is a test owner')

    def test_group_and_permission_association(self):
        # Test that an owner can be associated with groups and permissions
        self.owner.groups.add(self.group)
        self.owner.user_permissions.add(self.permission)
        self.assertIn(self.group, self.owner.groups.all())
        self.assertIn(self.permission, self.owner.user_permissions.all())

    def test_username_field(self):
        # Test that the USERNAME_FIELD is correctly set to 'email'
        self.assertEqual(Owner.USERNAME_FIELD, 'email')

    def test_unique_email(self):
        with self.assertRaises(Exception):
            Owner.objects.create(email='testowner@example.com')

    def test_string_representation(self):
        # Test that the string representation of owner model returns the email
        self.assertEqual(str(self.owner), 'testowner@example.com')
