from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """check if user with email address has been created"""
        email = "hello@gmail.com"
        password = "Test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@LONDONAPPDEV.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating with no email address raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_super_user(self):
        """test to create the superuser"""
        user = get_user_model().objects.create_superuser(
                "hello@gmail.com",
                "test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
