from django.test import RequestFactory, TestCase
from news.views import HomeNews, view_news
from news.models import News


class HomeNews_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        News.objects.create(title = 'test_title', content = 'test_content', is_published = True)

    def test_get_queryset_count(self):
        request = RequestFactory().get('/')
        view = HomeNews()
        view.setup(request)
        self.assertEquals(len(view.get_queryset()), 1)

    def test_get_queryset_content(self):
        request = RequestFactory().get('/')
        view = HomeNews()
        view.setup(request)
        self.assertEquals(view.get_queryset()[0].content, 'test_content')

    def test_get_queryset_category(self):
        request = RequestFactory().get('/')
        view = HomeNews()
        view.setup(request)
        self.assertEquals(view.get_queryset()[0].category, None)
