from django.test import TestCase
from news.models import News, Category

class NewsModel_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        News.objects.create(title = 'test_title', content = 'test_content', is_published = True)

    def test_str(self):
        news=News.objects.get(pk=1)
        str_pk_title = news.__str__()
        self.assertEquals(str_pk_title,'(1) test_title')

    def test_title(self):
        news=News.objects.get(pk=1)
        title = news.title
        self.assertEqual(title, 'test_title')
    
    def test_content(self):
        news=News.objects.get(pk=1)
        content = news.content
        self.assertEqual(content, 'test_content')
