import datetime
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from comments.models import Comment, Reply
from .models import Mystery, Instance, Release
from system.models import Group, Practical


# Create your tests here.


class ReleaseListTest(TestCase):
    """
    ReleaseList endpoint tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Sets up any models and relationships the tests depend on.
        """
        # custom user model
        cls.User = get_user_model()
        # test dependencies
        cls.user = cls.User.objects.create_user(username='test1',
                                                password='test1password')
        cls.practical = Practical.objects.create()
        cls.group = Group.objects.create(name='group1',
                                         practical=cls.practical)
        cls.user.group = cls.group
        cls.user.save()
        cls.mystery = Mystery.objects.create(name='mystery1')
        cls.instance = Instance.objects.create(group=cls.group,
                                               mystery=cls.mystery)
        cls.release1 = Release.objects.create(mystery=cls.mystery,
                                              number=1,
                                              clue="clue1",
                                              answer="answer1")
        cls.hash1 = cls.release1.hash
        cls.release2 = Release.objects.create(mystery=cls.mystery,
                                              number=2,
                                              clue="clue2",
                                              answer="answer2")
        cls.hash2 = cls.release2.hash
        cls.release3 = Release.objects.create(mystery=cls.mystery,
                                              number=3,
                                              clue="clue3",
                                              answer="answer3")
        cls.hash3 = cls.release3.hash

    def test_invalid_authentication(self):
        """
        If a non-registered user is making a release list request,
        HTTP_401_UNAUTHORIZED is returned in the response.
        """
        # auth token
        token = '12345'

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token)}

        # release list response
        response = self.client.get(reverse('mystery:release_list'), {},
                                   **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 401)

    def test_valid_list(self):
        """
        If a registered user who is part of a group and active mystery instance
        is making a release list request, a list of release data ordered by
        release number and HTTP_200_OK are returned in the response.
        """
        time = datetime.datetime.now()
        time = time - datetime.timedelta(days=7)
        with self.settings(START_DATETIME=time.strftime("%d/%m/%Y %H:%M:%S")):
            # auth token
            token = Token.objects.get(user__username='test1')

            # auth header
            header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

            # comment create response
            response = self.client.get(reverse('mystery:release_list'), {},
                                       **header)

            # run test
            # proper status code test
            self.assertEqual(response.status_code, 200)
            # returned comments test
            self.assertJSONEqual(response.content.decode('utf-8'),
                                 [
                                     {
                                         "commented": False,
                                         "number": 1
                                     },
                                     {
                                         "commented": False,
                                         "number": 2
                                     }
                                 ])

    def test_no_release(self):
        """
        If a registered user who is part of a group and inactive mystery
        instance is making a release list request, HTTP_400_BAD_REQUEST is
        returned in the response.
        """
        time = datetime.datetime.now()
        time = time + datetime.timedelta(days=1)
        with self.settings(START_DATETIME=time.strftime("%d/%m/%Y %H:%M:%S")):
            # auth token
            token = Token.objects.get(user__username='test1')

            # auth header
            header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

            # comment create response
            response = self.client.get(reverse('mystery:release_list'), {},
                                       **header)

            # run test
            # proper status code test
            self.assertEqual(response.status_code, 400)


class ArtifactTest(TestCase):
    """
    Artifact Endpoint Tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Sets up any models and relationships the tests depend on.
        """
        # custom user model
        cls.User = get_user_model()
        # test dependencies
        cls.user = cls.User.objects.create_user(username='test1',
                                                password='test1password')
        cls.practical = Practical.objects.create()
        cls.group = Group.objects.create(name='group1',
                                         practical=cls.practical)
        cls.user.group = cls.group
        cls.user.save()
        cls.mystery = Mystery.objects.create(name='mystery1')
        cls.mhash = cls.mystery.hash
        cls.instance = Instance.objects.create(group=cls.group,
                                               mystery=cls.mystery)
        cls.release1 = Release.objects.create(mystery=cls.mystery,
                                              number=1,
                                              clue="clue1",
                                              answer="answer1")
        cls.hash1 = cls.release1.hash
        cls.release2 = Release.objects.create(mystery=cls.mystery,
                                              number=2,
                                              clue="clue2",
                                              answer="answer2")
        cls.hash2 = cls.release2.hash
        cls.release3 = Release.objects.create(mystery=cls.mystery,
                                              number=3,
                                              clue="clue3",
                                              answer="answer3")
        cls.hash3 = cls.release3.hash

    def test_invalid_authentication(self):
        """
        If a non-registered user is making an artifact request,
        HTTP_401_UNAUTHORIZED is returned in the response.
        """
        # auth token
        token = '12345'

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token)}

        # release list response
        response = self.client.get(reverse('mystery:artifact_view',
                                           kwargs={'release': 1}), {},
                                   **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 401)

    def test_valid_release(self):
        """
        If a registered user who is part of a group and active mystery is
        making an artifact request for a release whose release date has been
        reached, a list of artifact data specific to the requested release and
        HTTP_200_OK are returned in the response.
        """
        time = datetime.datetime.now()
        time = time - datetime.timedelta(days=7)
        with self.settings(START_DATETIME=time.strftime("%d/%m/%Y %H:%M:%S")):
            # auth token
            token = Token.objects.get(user__username='test1')

            # auth header
            header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

            # comment create response
            response = self.client.get(reverse('mystery:artifact_view',
                                               kwargs={'release': 1}), {},
                                       **header)

            # run test
            # proper status code test
            self.assertEqual(response.status_code, 200)
            # returned comments test
            self.assertJSONEqual(response.content.decode('utf-8'),
                                 [
                                     {
                                         "clue": "clue1",
                                         "hash": self.hash1,
                                         "mystery_hash": self.mhash
                                     }
                                 ])

    def test_invalid_release(self):
        """
        If a registered user who is part of a group and active mystery is
        making an artifact request for a release whose release date has not yet
        been reached, HTTP_400_BAD_REQUEST is returned in the response.
        """

        time = datetime.datetime.now()
        time = time - datetime.timedelta(days=7)
        with self.settings(START_DATETIME=time.strftime("%d/%m/%Y %H:%M:%S")):
            # auth token
            token = Token.objects.get(user__username='test1')

            # auth header
            header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

            # comment create response
            response = self.client.get(reverse('mystery:artifact_view',
                                               kwargs={'release': 3}), {},
                                       **header)

            # run test
            # proper status code test
            self.assertEqual(response.status_code, 400)

    def test_dne_release(self):
        """
        If a registered user who is part of a group and active mystery is
        making an artifact request for a release that does not exist,
        HTTP_400_BAD_REQUEST is returned in the response.
        """

        time = datetime.datetime.now()
        time = time - datetime.timedelta(days=7)
        with self.settings(START_DATETIME=time.strftime("%d/%m/%Y %H:%M:%S")):
            # auth token
            token = Token.objects.get(user__username='test1')

            # auth header
            header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

            # comment create response
            response = self.client.get(reverse('mystery:artifact_view',
                                               kwargs={'release': 99}), {},
                                       **header)

            # run test
            # proper status code test
            self.assertEqual(response.status_code, 400)

    def test_no_release(self):
        """
        If a registered user who is part of a group and active mystery is
        making an artifact request without specifying a release,
        HTTP_400_BAD_REQUEST is returned in the response.

        NOTE: Not needed since handled by regex in django router
        """

        pass
