import unittest
from simple_scrapper import get_web_page
from simple_scrapper import keyword_look_up


class MyTestCase(unittest.TestCase):

    def test_get_web_page(self):
        web_page = get_web_page('http://parquestesistan.com/prototipos.html')
        self.assertIsInstance(web_page, str)

    def test_keyword_look_up(self):
        web_pages = ["<html> Erase una vez una magnolia que no aparecia </html>",
                     "<html> Aqui no hay nada mas que ceibas y sol, a lo mejor una magnolia </html>"]

        for web_page in web_pages:
            with self.subTest():
                result = keyword_look_up(web_page, 'Magnolia')
                self.assertTrue(result)

        for web_page in web_pages:
            with self.subTest():
                result = keyword_look_up(web_page, 'Lunatico')
                self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
