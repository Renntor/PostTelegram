from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from posts.models import Post


class PostTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            id=1000,
            telegram_id='test_1',
            telegram_name='test_1',
            is_superuser=True,
            is_staff=True
        )
        self.client.force_authenticate(user=self.user)

        self.post = Post.objects.create(
            id=1000,
            post_id=54498449,
            post='I love cats',
            owner=self.user
        )


    def test_destroy_post(self):
        response = self.client.delete(
            path='/posts/1000/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_create_post(self):

        response = self.client.post(
            path='/posts/',
            data={'id': 1001,
                  "post_id": 5444249,
                  "post": 'I love dogs',
                  'owner': self.user.id
                  }
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_post(self):
        response = self.client.patch(
            path='/posts/1000/',
            data={'post': 'I love dogs'}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_get_post(self):
        response = self.client.get(
            '/posts/1000/'
        )
        self.assertEquals(
            response.data['post'],
            'I love cats'
        )



