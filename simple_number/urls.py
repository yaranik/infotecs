# Povolotsky Yaroslav# 2018from django.conf.urls import urlfrom . import views# url для стартовой страницы и страницы резельтатаurlpatterns = [    url(r'^$', views.MyForm.search, name='search'),    url(r'^result/$', views.MyForm.result, name='result'),]