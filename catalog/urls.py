from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'), # отображение главной страницы сайта (функция с именем index в views.py
    url(r'^contracts/$', views.ContractListView.as_view(), name='contracts'),# ссылка на catalog/contracts
    url(r'^contract/(?P<pk>\d+)$', views.ContractDetailView.as_view(), name='contract-detail'), #подробное описание договора
]