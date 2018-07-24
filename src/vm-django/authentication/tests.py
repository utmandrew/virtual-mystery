from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your tests here.


class LoginTest(TestCase):
    """
    Login tests.
    """

    def test_valid_credentials(self):
        """
        If username and password credentials match that of a registered user,
        the user's authentication token and http_200_ok are returned in the
        response.
        """
        # test case setup
        user = User.objects.create_user(username="Test1",
                                        email="Test1@example.com",
                                        password="12345")
        token = Token.objects.get(user__username='Test1')

        data = {'username': "Test1", 'password': "12345"}

        # sends login request
        response = self.client.post(reverse('authentication:token'), data)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 200)
        # user token test
        self.assertEqual(response.data['token'], token.key)
        # test case breakdown
        user.delete()

    def test_invalid_username(self):
        """
        If username credential does not match that of a registered
        user, http_400_bad_request is returned in the response.
        """
        # test case setup
        user = User.objects.create_user(username="Test1",
                                        email="Test1@example.com",
                                        password="12345")

        data = {'username': "Test2", 'password': "12345"}

        # sends login request
        response = self.client.post(reverse('authentication:token'), data)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 400)

        # test case breakdown
        user.delete()

    def test_invalid_password(self):
        """
        If password credential does not match that of the username of a
        registered user, http_400_bad_request is returned in the response.
        """
        # test case setup
        user = User.objects.create_user(username="Test1",
                                        email="Test1@example.com",
                                        password="12345")

        data = {'username': "Test1", 'password': "123"}

        # sends login request
        response = self.client.post(reverse('authentication:token'), data)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 400)

        # test case breakdown
        user.delete()

    def test_no_credentials(self):
        """
        If no username or password is provided, http_400_bad_request is
        returned in the response.
        """
        # test case setup
        user = User.objects.create_user(username="Test1",
                                        email="Test1@example.com",
                                        password="12345")

        data = {'username': "", 'password': ""}

        # sends login request
        response = self.client.post(reverse('authentication:token'), data)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 400)

        # test case breakdown
        user.delete()

    def test_no_username(self):
        """
        If no username is provided, http_400_bad_request is returned in the
        response.
        """
        # test case setup
        user = User.objects.create_user(username="Test1",
                                        email="Test1@example.com",
                                        password="12345")

        data = {'username': "", 'password': "123"}

        # sends login request
        response = self.client.post(reverse('authentication:token'), data)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 400)

        # test case breakdown
        user.delete()

    def test_no_password(self):
        """
        If no password is provided, http_400_bad_request is returned in the
        response.
        """
        # test case setup
        user = User.objects.create_user(username="Test1",
                                        email="Test1@example.com",
                                        password="12345")

        data = {'username': "Test1", 'password': ""}

        # sends login request
        response = self.client.post(reverse('authentication:token'), data)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 400)

        # test case breakdown
        user.delete()


class LogoutTest(TestCase):
    """
    Logout Tests.
    """

    def test_valid_logout(self):
        """
        If the authentication credential (token) matches that of a registered
        user, the user's authentication token is deleted and http_200_ok is
        returned in the response.
        """
        # test case setup
        user = User.objects.create_user(username="Test1",
                                        email="Test1@example.com",
                                        password="12345")

        token1 = Token.objects.get(user__username='Test1')

        data = {'username': "Test1", 'password': "12345"}

        # sends login request
        response = self.client.post(reverse('authentication:token'), data)

        # login test
        # proper status code test
        self.assertEqual(response.status_code, 200)
        # user token test
        self.assertEqual(response.data['token'], token1.key)

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token1.key)}

        # send logout request
        response = self.client.get(reverse('authentication:logout'), {},
                                   **header)

        # logout test
        # proper status code test
        self.assertEqual(response.status_code, 200)

        # sends login request
        response = self.client.post(reverse('authentication:token'), data)

        # login test
        # proper status code test
        self.assertEqual(response.status_code, 200)

        # get new token
        token2 = Token.objects.get(user__username='Test1')

        # user token test
        self.assertNotEqual(token2.key, token1.key)

        # test case breakdown
        user.delete()

    def test_invalid_logout(self):
        """
        If the authentication credential (token) does not matches that of a
        registered user, the user's authentication token is not deleted and
        http_401_unauthorized is returned in the response.
        """
        # test case setup
        user = User.objects.create_user(username="Test1",
                                        email="Test1@example.com",
                                        password="12345")

        token1 = Token.objects.get(user__username='Test1')

        data = {'username': "Test1", 'password': "12345"}

        # sends login request
        response = self.client.post(reverse('authentication:token'), data)

        # login test
        # proper status code test
        self.assertEqual(response.status_code, 200)
        # user token test
        self.assertEqual(response.data['token'], token1.key)

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(
            'abc123def456ghi789jkl123abc456def789ghi0')}

        # send logout request
        response = self.client.get(reverse('authentication:logout'), {},
                                   **header)

        # new token
        token2 = Token.objects.get(user__username='Test1')

        # logout test
        # proper status code test
        self.assertEqual(response.status_code, 401)
        # user token test
        self.assertEqual(token2.key, token1.key)

        # test case breakdown
        user.delete()
