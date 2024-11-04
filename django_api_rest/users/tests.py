from django.urls import reverse_lazy
from rest_framework.test import APITestCase


class UserTest(APITestCase):
    url = reverse_lazy('user')
