from django.shortcuts import render

from .models import Company, ConstructionObject, Contract, ManagerPerson

import datetime

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" договоров, организаций и объектов строительства
    num_contracts=Contract.objects.all().count()
    num_companys=Company.objects.all().count()
    num_objects=ConstructionObject.objects.all().count()
    # Подписанные договора (статус = 's') - signed
    num_contracts_signed=Contract.objects.filter(contract_status__exact='s').count()
    # Текущая дата в формате: день.месяц.год
    date_now = datetime.datetime.now().strftime("%d.%m.%Y")
    # Отрисовка HTML-шаблона index.html с данными внутри переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_contracts':num_contracts,'num_companys':num_companys,
                 'num_objects':num_objects,'num_contracts_signed':num_contracts_signed, 
                 'date_now':date_now},
    )

# отображение класса contract
from django.views import generic

class ContractListView(generic.ListView):
    model = Contract
    
class ContractDetailView(generic.DetailView):
    model = Contract
    def get_object(self):
        # Call the superclass
        object = super(ContractDetailView, self).get_object()
        # вычисление времени нахождения договора в работе (кол-во дней)
        if object.date_work_note:
            object.work_time = datetime.datetime.now().date() - object.date_work_note # если есть дата СЗ
        else:
            object.work_time = datetime.datetime.now().date() - object.publish.date() # если нет даты СЗ (от даты записи)
        object.save()
        return object

# отображение класса Company
class CompanyListView(generic.ListView):
    model = Company

class CompanyDetailView(generic.DetailView):
    model = Company

# отображение класса ConstructionObject
class ConstructionObjectListView(generic.ListView):
    model = ConstructionObject

class ConstructionObjectDetailView(generic.DetailView):
    model = ConstructionObject
"""
from django.views.generic import DetailView
from django.utils import timezone
from books.models import Author

class AuthorDetailView(DetailView):

    queryset = Author.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(AuthorDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object
        """