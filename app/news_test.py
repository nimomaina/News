import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
        '''
        Test class to test the behavior of the news source class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_source = News('abc', 'nimo', 'https://abc.com/', 'abc news is the best source', 'usa',
                                        'general', 'abc-news')

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_source, News))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_source.name, 'abc')
            self.assertEquals(self.new_source.author, 'nimo')
            self.assertEquals(self.new_source.url, 'https://abc.com/')
            self.assertEquals(self.new_source.description, 'abc news is the best source')
            self.assertEquals(self.new_source.country, 'usa')
            self.assertEquals(self.new_source.category, 'general')
            self.assertEquals(self.new_source.id, 'abc-news')


if __name__ == '__main__':
    unittest.main()