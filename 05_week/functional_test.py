from selenium import webdriver

import unittest


class FunctionalTest(unittest.TestCase):
    def setUp(self):
        path = './chromedriver'
        # Django 8000 port, html title Django 포함
        self.driver = webdriver.Chrome(path)

    def tearDown(self):
        self.driver.quit()

    def test_has_worked_in_title(self):

        # driver.get('http://www.facebook.org')
        self.driver.get('http://localhost:8000')

        # assert "worked" in driver.title
        self.assertIn("worked", self.driver.title)

    def test_has_install_in_title(self):
        self.driver.get('http://localhost:8000')

        self.assertIn("install", self.driver.title)