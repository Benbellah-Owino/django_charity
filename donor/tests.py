# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Donor


class DonorModelTestCase(TestCase):
    def setUp(self):
        # Create test data for the Donor model
        self.donor = Donor.objects.create(
            email='test@example.com',
            username='testuser',
            phone='1234567890',
            gender='M',
            total_donated=100
        )
        # Create test groups
        self.group = Group.objects.create(name='Test Group')

        # Create content type for Donor model
        self.content_type = ContentType.objects.get_for_model(Donor)

        # Create test permission associated with Donor model
        self.permission = Permission.objects.create(
            name='Test Permission',
            codename='test_permission',
            content_type=self.content_type
        )

    def test_donor_creation(self):
        # Test that a Donor object is created successfully
        self.assertEqual(self.donor.email, 'test@example.com')
        self.assertEqual(self.donor.username, 'testuser')
        self.assertEqual(self.donor.phone, '1234567890')
        self.assertEqual(self.donor.gender, 'M')
        self.assertEqual(self.donor.total_donated, 100)

    def test_group_and_permission_association(self):
        # Test that a Donor can be associated with groups and permissions
        self.donor.groups.add(self.group)
        self.donor.user_permissions.add(self.permission)
        self.assertIn(self.group, self.donor.groups.all())
        self.assertIn(self.permission, self.donor.user_permissions.all())

    def test_username_field(self):
        # Test that the USERNAME_FIELD is correctly set to 'email'
        self.assertEqual(Donor.USERNAME_FIELD, 'email')

    def test_unique_email(self):
        # Test that email field is unique
        with self.assertRaises(Exception):
            Donor.objects.create(email='test@example.com')

    def test_string_representation(self):
        # Test that the string representation of Donor model returns the email
        self.assertEqual(str(self.donor), 'test@example.com')
