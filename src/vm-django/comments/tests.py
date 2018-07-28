import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Comment, Reply
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
                                             password='test1password')
        cls.practical = Practical.objects.create()
        cls.group = Group.objects.create(name='group1',
                                         practical=cls.practical)
        cls.user.profile.group = cls.group
        cls.user.profile.save()
        cls.mystery = Mystery.objects.create(name='mystery1')
        cls.instance = Instance.objects.create(group=cls.group,
                                                mystery=cls.mystery)

    def test_invalid_authentication(self):
        """
        If a non-registered user is commenting on a current release for the first
        time, http_401_unauthorized is returned in the response and no comment
        is created.
        """
        # auth token
        token = '12345'
        # comment create data
        data = {'text': 'first comment'}

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token)}

        # comment create response
        response = self.client.post(reverse('comment:comment_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 401)
        # comment created test
        self.assertFalse(Comment.objects.filter(owner=self.user,
                                               instance=self.instance,
                                               text='first comment1').exists())

    def test_missing_data(self):
        """
        If a registered user is commenting on a current release for the first
        time with missing request data (text), http_400_bad_request is returned
        in the response and no comment is created.
        """
        # auth token
        token = Token.objects.get(user__username='test1')
        # comment create data
        data = {}

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

        # comment create response
        response = self.client.post(reverse('comment:comment_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 400)
        # comment created test
        self.assertFalse(Comment.objects.filter(owner=self.user,
                                               instance=self.instance,
                                               text='first comment').exists())

    def test_valid_comment(self):
        """
        If a registered user is commenting on a current release for the first
        time, http_201_created is returned in the response and the comment is
        created.
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
        # comment created test
        self.assertTrue(Comment.objects.filter(owner=self.user,
                                            instance=self.instance,
                                                text='first comment').exists())


    def test_multi_comment(self):
        """
        If a registered user is commenting on a current release more than one
        time, http_403_forbidden is returned in the response and no comment is
        created.
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
        # comment created test
        self.assertTrue(Comment.objects.filter(owner=self.user,
                                               instance=self.instance,
                                               text='first comment').exists())

        # comment create data
        data = {'text': 'second comment'}

        # comment create response
        response = self.client.post(reverse('comment:comment_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 403)
        # comment created test
        self.assertFalse(Comment.objects.filter(owner=self.user,
                                               instance=self.instance,
                                               text='second comment').exists())

    def test_no_release(self):
        """
        If a registered user is commenting before the mystery is released,
        http_400_forbidden is returned in the response and no comment is
        created.
        """
        time = datetime.datetime.now()
        time = time + datetime.timedelta(days=1)
        with self.settings(START_DATETIME=time.strftime("%d/%m/%Y %H:%M:%S")):
            # auth token
            token = Token.objects.get(user__username='test1')
            # comment create data
            data = {'text': 'first comment'}

            # auth header
            header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

            # comment create response
            response = self.client.post(reverse('comment:comment_create'),
                                        data, **header)

            # run test
            # proper status code test
            self.assertEqual(response.status_code, 400)
            # comment created test
            self.assertFalse(Comment.objects.filter(owner=self.user,
                                                instance=self.instance,
                                                text='first comment').exists())


class CommentListTest(TestCase):
    """
    CommentList endpoint tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Sets up any models and relationships the tests depend on.
        """
        # commented
        cls.user = User.objects.create_user(username='test1',
                                            password='test1password')

        # commented
        cls.user2 = User.objects.create_user(username='test2',
                                            password='test2password')

        # not commented
        cls.user3 = User.objects.create_user(username='test3',
                                             password='test3password')

        cls.practical = Practical.objects.create()
        cls.group = Group.objects.create(name='group1',
                                         practical=cls.practical)
        cls.user.profile.group = cls.group
        cls.user.profile.save()

        cls.user2.profile.group = cls.group
        cls.user2.profile.save()

        cls.user3.profile.group = cls.group
        cls.user3.profile.save()

        cls.mystery = Mystery.objects.create(name='mystery1')
        cls.instance = Instance.objects.create(group=cls.group,
                                               mystery=cls.mystery)

    def setUp(self):
        """
        Run before every test.
        """
        # first comment
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
        # comment created test
        self.assertTrue(Comment.objects.filter(owner=self.user,
                                              instance=self.instance,
                                              text='first comment').exists())

        # save comment id
        self.comment = Comment.objects.filter(owner=self.user,
                                              instance=self.instance,
                                              text='first comment')[0].id

        # first reply
        # auth token
        token = Token.objects.get(user__username='test2')
        # reply create data
        data = {'text': 'first reply', 'parent': str(self.comment)}

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

        # reply create response
        response = self.client.post(reverse('comment:reply_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 201)
        # reply created test
        self.assertTrue(Reply.objects.filter(owner=self.user2,
                                             parent=self.comment,
                                             text='first reply').exists())

        # save reply id
        self.reply = Reply.objects.filter(owner=self.user2,
                                               parent=self.comment,
                                               text='first reply')[0].id

        # second reply
        # auth token
        token = Token.objects.get(user__username='test1')
        # reply create data
        data = {'text': 'second reply', 'parent': str(self.comment)}

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

        # reply create response
        response = self.client.post(reverse('comment:reply_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 201)
        # reply created test
        self.assertTrue(Reply.objects.filter(owner=self.user,
                                             parent=self.comment,
                                             text='second reply').exists())

        # save reply id
        self.reply2 = Reply.objects.filter(owner=self.user,
                                          parent=self.comment,
                                          text='second reply')[0].id

        # second comment
        # auth token
        token = Token.objects.get(user__username='test2')
        # comment create data
        data = {'text': 'second comment'}

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

        # comment create response
        response = self.client.post(reverse('comment:comment_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 201)
        # comment created test
        self.assertTrue(Comment.objects.filter(owner=self.user2,
                                               instance=self.instance,
                                               text='second comment').exists())

        # save comment id
        self.comment2 = Comment.objects.filter(owner=self.user2,
                                              instance=self.instance,
                                              text='second comment')[0].id

    def test_invalid_authentication(self):
        """
        If a non-registered user is requesting a list of comments for a
        specific release which they had commented on, http_401_unauthorized is
        returned in the response and no comments are returned.
        """
        time = datetime.datetime.now()
        time = time - datetime.timedelta(hours=1)
        with self.settings(START_DATETIME=time.strftime("%d/%m/%Y %H:%M:%S")):
            # auth token
            token = '12345'

            # auth header
            header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token)}

            # comment create response
            response = self.client.get(reverse('comment:comment_list',
                                               kwargs={'release': 1}),
                                       {}, **header)

            # run test
            # proper status code test
            self.assertEqual(response.status_code, 401)
            # returned comments test
            self.assertJSONEqual(response.content.decode('utf-8'),
                {'detail': 'Invalid token.'})

    def test_no_comment(self):
        """
        If a registered user is requesting a list of comments for a specific
        release which they had not commented on (includes non-existent release)
        , http_403_forbidden is returned in the response and no comments are
        returned.
        """
        time = datetime.datetime.now()
        time = time - datetime.timedelta(hours=1)
        with self.settings(START_DATETIME=time.strftime("%d/%m/%Y %H:%M:%S")):
            # auth token
            token = Token.objects.get(user__username='test3')

            # auth header
            header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

            # comment create response
            response = self.client.get(reverse('comment:comment_list',
                                               kwargs={'release': 1}),
                                       {}, **header)

            # run test
            # proper status code test
            self.assertEqual(response.status_code, 403)
            # returned comments test
            self.assertEqual(response.content, b'')

    def test_valid_list(self):
        """
        If a registered user is requesting a list of comments for a
        specific release which they had commented on, http_200_ok
        and a sorted list comments are returned in the response.
        """

        time = datetime.datetime.now()
        time = time - datetime.timedelta(hours=1)
        with self.settings(START_DATETIME=time.strftime("%d/%m/%Y %H:%M:%S")):
            # auth token
            token = Token.objects.get(user__username='test1')

            # auth header
            header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

            # comment create response
            response = self.client.get(reverse('comment:comment_list',
                                               kwargs={'release': 1}),
                                               {}, **header)

            # run test
            # proper status code test
            self.assertEqual(response.status_code, 200)
            # returned comments test
            self.assertJSONEqual(response.content.decode('utf-8'),
                                 [
                                     {
                                         "id": self.comment,
                                         "reply": [
                                             {
                                                 "id": self.reply,
                                                 "text": "first reply",
                                                 "username": "test2"
                                             },
                                             {
                                                 "id": self.reply2,
                                                 "text": "second reply",
                                                 "username": "test1"
                                             },
                                         ],
                                         "text": "first comment",
                                         "username": "test1"
                                     },
                                     {
                                         "id": self.comment2,
                                         "reply": [],
                                         "text": "second comment",
                                         "username": "test2"
                                     }
                                 ])


class ReplyCreateTest(TestCase):
    """
    ReplyCreate endpoint tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Sets up any models and relationships the tests depend on.
        Run once at the beginning.
        """
        cls.user = User.objects.create_user(username='test1',
                                            password='test1password')
        cls.practical = Practical.objects.create()
        cls.group = Group.objects.create(name='group1',
                                         practical=cls.practical)
        cls.user.profile.group = cls.group
        cls.user.profile.save()
        cls.mystery = Mystery.objects.create(name='mystery1')
        cls.instance = Instance.objects.create(group=cls.group,
                                               mystery=cls.mystery)

    def setUp(self):
        """
        Run before every test.
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
        # comment created test
        self.assertTrue(Comment.objects.filter(owner=self.user,
                                              instance=self.instance,
                                              text='first comment').exists())

        # save comment id
        self.comment = Comment.objects.filter(owner=self.user,
                                             instance=self.instance,
                                             text='first comment')[0].id

    def test_invalid_authentication(self):
        """
        If a non-registered user is replying to a comment in their current
        release, http_401_unauthorized is returned in the response and no reply
        is created.
        """
        # auth token
        token = '12345'

        # reply create data
        data = {'text': 'first comment', 'parent': str(self.comment)}

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token)}

        # reply create response
        response = self.client.post(reverse('comment:reply_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 401)
        # reply created test
        self.assertFalse(Reply.objects.filter(owner=self.user,
                                              parent=self.comment,
                                              text='first comment').exists())

    def test_missing_data(self):
        """
        If a registered user is replying to a comment in their current release
        with missing request data (parent), http_400_bad_request is returned in
        the response and no reply is created.
        """
        # auth token
        token = Token.objects.get(user__username='test1')
        # reply create data
        data = {}

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

        # reply create response
        response = self.client.post(reverse('comment:reply_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 400)
        # reply created test
        self.assertFalse(Reply.objects.filter(owner=self.user,
                                             parent=self.comment,
                                             text='first comment').exists())

    def test_valid_reply(self):
        """
        If a registered user is replying to a comment in their current release,
        http_201_created is returned and the reply is created.
        """
        # auth token
        token = Token.objects.get(user__username='test1')
        # reply create data
        data = {'text': 'first comment', 'parent': str(self.comment)}

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

        # reply create response
        response = self.client.post(reverse('comment:reply_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 201)
        # reply created test
        self.assertTrue(Reply.objects.filter(owner=self.user,
                                              parent=self.comment,
                                              text='first comment').exists())

    def test_parent_dne(self):
        """
        If a registered user is replying to a non-existent comment in their
        current release, http_400_bad_request is returned and no reply is
        created.
        """
        # auth token
        token = Token.objects.get(user__username='test1')
        # reply create data
        data = {'text': 'first comment', 'parent': str(self.comment + 1)}

        # auth header
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.key)}

        # reply create response
        response = self.client.post(reverse('comment:reply_create'), data,
                                    **header)

        # run test
        # proper status code test
        self.assertEqual(response.status_code, 400)
        # reply created test
        self.assertFalse(Reply.objects.filter(owner=self.user,
                                             parent=self.comment,
                                             text='first comment').exists())
