from django.shortcuts import render

from .models import Company, ConstructionObject, Contract

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
    
    # Отрисовка HTML-шаблона index.html с данными внутри переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_contracts':num_contracts,'num_companys':num_companys,
                 'num_objects':num_objects,'num_contracts_signed':num_contracts_signed},
    )

# отображение класса contract
from django.views import generic

class ContractListView(generic.ListView):
    model = Contract
    
class ContractDetailView(generic.DetailView):
    model = Contract