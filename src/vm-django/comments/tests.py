from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from mystery.models import Mystery, Instance
from system.models import Profile, Group, Practical

# Create your tests here.


class CommentCreateTest(TestCase):
    """
    CommentCreate endpoint tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Sets up any models and relationships the tests depend on.
        """
        cls.user = User.objects.create_user(username='test1',
                                             password='test1')
        print(cls.user)
        # cls.practical = Practical.objects.create()
        cls.group = Group.objects.create(name='group1')
        print(cls.group)
        # cls.user.profile.group = cls.group
        cls.profile = Profile.objects.filter(user=cls.user.id)
        print(cls.profile)
        cls.profile[0].group = cls.group
        cls.profile[0].save()
        cls.mystery = Mystery.objects.create(name='mystery1')
        print(cls.mystery)
        cls.instance = Instance.objects.create(group=cls.group,
                                                mystery=cls.mystery)
        print(cls.instance)

    def test_invalid_authentication(self):
        """
        If a non-registered user is commenting on a current release for the first
        time, http_401_unauthorized is returned in the response.
        """
        pass

    def test_missing_data(self):
        """
        If a registered user is commenting on a current release for the first
        time with missing request data (text), http_400_bad_request is returned
        in the response.
        """
        pass

    def test_valid_comment(self):
        """
        If a registered user is commenting on a current release for the first
        time, http_201_created is returned in the response.
        """
        # auth token
        token = Token.objects.get(user__username='test1')
        # comment create data
        data = {'text': 'first comment'}

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

        # comment create response
        response = self.client.post(reverse('comment:comment_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 201)


    def test_multi_comment(self):
        """
        If a registered user is commenting on a current release more than one
        time, http_403_forbidden is returned in the response.
        """
        pass

    def test_no_release(self):
        """
        If a registered user is commenting before the mystery is released,
        http_403_forbidden is returned in the response.
        """
        pass


class CommentListTest(TestCase):
    """
    CommentList endpoint tests.
    """

    def setUp(self):
        """
        Sets up any models and relationships the tests depend on.
        """
        pass

    def test_invalid_authentication(self):
        """
        If a non-registered user is requesting a list of comments for a
        specific release which they had commented on, http_401_unauthorized is
        returned in the response.
        """
        pass

    def test_no_comment(self):
        """
        If a registered user is requesting a list of comments for a specific
        release which they had not commented on (includes non-existent release)
        , http_403_forbidden is returned in the response.
        """
        pass

    def test_valid_list(self):
        """
        If a registered user is requesting a list of comments for a
        specific release which they had commented on, http_200_ok
        and a sorted list comments are returned in the response.
        """
        pass


class ReplyCreateTest(TestCase):
    """
    ReplyCreate endpoint tests.
    """

    def setUp(self):
        """
        Sets up any models and relationships the tests depend on.
        """
        pass

    def test_invalid_authentication(self):
        """
        If a non-registered user is replying to a comment in their current
        release, http_401_unauthorized is returned in the response.
        """
        pass

    def test_missing_data(self):
        """
        If a registered user is replying to a comment in their current release
        with missing request data (parent), http_400_bad_request is returned in
        the response.
        """
        pass

    def test_valid_reply(self):
        """
        If a registered user is replying to a comment in their current release,
        http_201_created is returned.
        """
        pass

    def test_parent_dne(self):
        """
        If a registered user is replying to a non-existent comment in their
        current release, http_400_bad_request is returned.
        """
        pass
