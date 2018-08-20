# Povolotsky Yaroslav
# 2018
from django.shortcuts import render_to_response
from .myfunc import MyFunction
from django.http import HttpResponse

# Функции управления формами


class MyForm:

    @staticmethod
    def search(request):  # функция вызова стартовой страницы
        return render_to_response('simple_number/general_page.html')

    @staticmethod
    def result(request):  # функция реакции на запрос

        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']

            if q.isdecimal() is True and q.startswith('0') is False and q != '1':
                # проверка введеного числа в поле
                return render_to_response('simple_number/search_page.html',
                                      {'query': MyFunction.simple_num(int(q))})   # вывод при корретном вводе
            elif q == '1':  # проверка введеного числа в поле, вывод в случае 1
                return render_to_response('simple_number/search_page.html',
                                      {'query': [1]})
            else:  # проверка введеного числа в поле, вывод в случае ошибки
                return render_to_response('simple_number/search_page.html',
                                      {'query': 'Введите натуральное число!'})

        elif 'q' in request.GET and request.GET['q'] == '':  # проверка на пустую форму
            return render_to_response('simple_number/search_page.html',
                                      {'query': 'Введите натуральное число!'})




