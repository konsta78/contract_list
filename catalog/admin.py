from django.contrib import admin
from .models import Company, Contract, ConstructionObject, ManagerPerson

# класс отображения информации о подписанте

class ManagerPersonAdmin(admin.ModelAdmin):
    list_display = ('manager_name', 'manager_position', 'manager_company', 'manager_signature')
    
admin.site.register(ManagerPerson, ManagerPersonAdmin)

# класс меняет отобращение информации о моделе "Contract"
class ContractAdmin(admin.ModelAdmin):
    list_display = ('number', 'date_of_conclusion', 'customer', 'executor', 'contract_status', 'constr_object')
    list_filter = ('customer', 'executor', 'contract_status', 'constr_object')

admin.site.register(Contract, ContractAdmin)

# регистрация класса CompanyAdmin посредством декоратора
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'phone')
    
# регистрация класса ConstructionObject
@admin.register(ConstructionObject)
class ConstructionObjectAdmin(admin.ModelAdmin):
    list_display = ('line', 'requisites')