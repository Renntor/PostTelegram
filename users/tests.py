from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            id=500,
            telegram_id='test',
            telegram_name='test',
            is_superuser=True,
            is_staff=True
        )

        self.client.force_authenticate(user=self.user)

    def test_destroy_user(self):
        response = self.client.delete(
            '/users/500/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_create_user(self):
        response = self.client.post(
            '/users/',
            {'id': 501,
             "telegram_id": 'test_2',
             "telegram_name": 'test_2',
             }
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_user(self):
        response = self.client.patch(
            '/users/500/',
            {"telegram_id": 'new_test'}
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.data['telegram_id'],
            'new_test'
        )

    def test_get_user(self):
        response = self.client.get(
            '/users/500/'
        )

        self.assertEquals(
            response.data['telegram_id'],
            'test'
        )
