from django.test import SimpleTestCase
from django.urls import reverse, resolve

from news.views import register, user_login, feedback, NewsByCategory

class Urls_test(SimpleTestCase):

    def test_register_is_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_login_is_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, user_login)

    def test_feedback_is_resolves(self):
        url = reverse('feedback')
        self.assertEquals(resolve(url).func, feedback)
