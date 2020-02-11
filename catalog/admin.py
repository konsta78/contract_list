from django.contrib import admin
from .models import Company, Contract, ConstructionObject

# класс меняет отобращение информации о моделе "Contract"
class ContractAdmin(admin.ModelAdmin):
    list_display = ('number', 'date_of_conclusion', 'customer', 'executor', 'contract_status', 'constr_object')
    list_filter = ('customer', 'executor', 'contract_status', 'constr_object')

admin.site.register(Contract, ContractAdmin)

# регистрация класса CompanyAdmin посредством декоратора
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'manager', 'manager_position', 'signature')
    
# регистрация класса ConstructionObject
@admin.register(ConstructionObject)
class ConstructionObjectAdmin(admin.ModelAdmin):
    list_display = ('line', 'requisites')