"""
authentication app tests
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):
    """
    user manager tests
    """
    def test_create_user(self):
        """
        test create user function
        """
        user_model = get_user_model()
        user = user_model.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertIsNone(user.username)
    
            
        with self.assertRaises(TypeError):
            user_model.objects.create_user()
        with self.assertRaises(TypeError):
            user_model.objects.create_user(email='')
        with self.assertRaises(ValueError):
            user_model.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        """
        test create superuser function
        """
        user_model = get_user_model()
        admin_user = user_model.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertIsNone(admin_user.username)

        with self.assertRaises(ValueError):
            user_model.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)