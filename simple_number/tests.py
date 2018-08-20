# Povolotsky Yaroslav
# 2018
from django.test import TestCase
from .myfunc import MyFunction
from .views import MyForm
from django.test.client import RequestFactory
import unittest

# Тест функции определения простых множителей числа


class TestForMyFunction(unittest.TestCase):

    def setUp(self):
        self.MyFunction = MyFunction()

    def test_func(self):
        self.assertEqual(MyFunction.simple_num(10), [2, 5])

# Тест формы(переходы на определеные url)


class TestForMyForm(TestCase):

    def setUp(self):
        self.MyForm = RequestFactory()

    def test_search(self):
        request = self.MyForm.get('/')
        response = MyForm.search(request)
        self.assertEqual(response.status_code, 200)

    def test_result(self):
        request = self.MyForm.get('/result/?q=10')
        response = MyForm.result(request)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()