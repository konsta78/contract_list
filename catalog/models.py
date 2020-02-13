from django.db import models
from django.urls import reverse # Используется для генерации URL путем изменения шаблонов URL
from django.utils import dateformat

# Мои модели здесь!

class Company(models.Model):
    """
    Модель представляет собой описание организации/контрагента
    Наименование (полное и сокращенное), подписант (ФИО), должность подписанта, основание (устав, доверенность)
    """
    # полное наименование организации
    name = models.CharField(max_length=300, verbose_name="Полное наименование организации")
    
    # сокращенное наименование организации
    short_name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    
    # ФИО подписанта
    manager = models.CharField(max_length=100, verbose_name="ФИО подписанта")
    
    # должность подписанта
    manager_position = models.CharField(max_length=200, verbose_name="Должность подписанта")
    
    # основание для подписи (устав или доверенность)
    grounds_for_signature = (
        ('charter', 'Устав'), 
        ('power_of_attorney', 'Доверенность')
    )
    signature = models.CharField(max_length=17, choices=grounds_for_signature, default='charter', 
                                 verbose_name="Основание для подписи")
    
    class Meta:
        ordering = ["short_name"] # сортировка организаций по сокращенному наименованию
    
    def __str__(self):
        """
        Возвращает название организации по сокращенному названию
        """
        return self.short_name
    
    def get_absolute_url(self):
        """
        Возвращает URL с подродбным описанием Организации
        """
        return reverse('company-detail', args=[str(self.id)])
    
class Contract(models.Model):
    """
    Модель представляет собой описание Договора:
    Номер, Заказчик и исполнитель (от Company), предмет договора (краткое описание),
    срок действия, дата заключения, сумма договора, 
    тип договора (ЭС, ВС и т.д., статус (подписан, на подпсании, аннулирован, расторгнут), 
    объект строительства (от ConstructionObject), контактное лицо в ДО (от Contract_department), 
    № служебной записки (от Contract_department), наличие дополнительных соглашений (от Supplementary_contract)
    """
    # номер договора
    number = models.CharField(max_length=50, verbose_name="Номер договора")
    
    # заказчик
    customer = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, verbose_name="Заказчик",
                                 related_name = 'Company_customer')
    
    # исполнитель
    executor = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, verbose_name="Исполнитель",
                                 related_name = 'Company_executor')
    
    # предмет договора (краткое описание)
    subject_of_contract = models.TextField(max_length=500, verbose_name="Предмет договора")
    
    # окончание срока действия договора
    contract_time = models.DateField(null=True, blank=True, verbose_name="Срок действия договора")
    
    # дата заключения
    date_of_conclusion = models.DateField(null=True, blank=True, verbose_name="Дата заключения договора")
    
    # сумма по договору
    
    # тип договора (ЭС, ВС и ВО, ТС, ГС, разное)
    
    # статус (подписан, на подписании, аннулирован, расторгнут
    status = (
        ('s', 'Подписан'),
        ('o', 'На подписании'),
        ('c', 'Аннулирован'),
        ('t', 'Расторгнут'),
    )
    contract_status = models.CharField(max_length=13, choices=status, default='o', verbose_name="Статус договора")
    
    # объект строительства
    constr_object = models.ForeignKey('ConstructionObject', on_delete=models.SET_NULL, null=True, 
                                      verbose_name="Объект строительства", 
                                      related_name = 'ConstructionObject_constr_object')
    
    # Номер и дата служебной записки
    num_work_note = models.IntegerField(null=True, blank=True, verbose_name="Номер служебной записки")
    date_work_note = models.DateField(null=True, blank=True, verbose_name="Дата служебной записки")
    publish = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи") # дата создания записи (не видна в админке)
    
    # контактное лицо в Договорном отделе
    person_name = (
        ('1', 'Павлышко Екатерина Сергеевна'),
        ('2', 'Пуленкова Римма Николаевна'),
        ('3', 'Бочков Максим Александрович'),
        ('4', 'Великородная Оксана Леонидовна')
    )
    person = models.CharField(max_length=20, choices=person_name, default='Павлышко Е. С.', verbose_name="Контактное лицо ДО")
    
    
    class Meta:
        ordering = ["contract_status"] # сортировка договоров по статусу   
    
    def __str__(self):
        """
        Возвращает название договора по его номеру
        """
        return self.number
    
    def get_absolute_url(self):
        """
        Возвращает URL с подродбным описанием параметров Договора
        """
        return reverse('contract-detail', args=[str(self.id)])
    
class ConstructionObject(models.Model):
    """
    Модель описывает объект строительства - к какой линии (государственному контракту) относится строящийся объект,
    а также реквизиты банка в соответствии с ГК.
    Невско-Василеостровская линия (НВЛ), Фрунзенский радиус (Ф-2), Лахтинско-Правобережная линиия (ЛПЛ),
    Красносельско-Калининская линия (ККЛ) или другое (общие договоры)
    """
    # наименовании объекта строительства (линия)
    line_name = (
        ('НВЛ', 'Невско-Василеостровская линия'),
        ('Ф-2', 'Фрунзенский радиус'),
        ('ЛПЛ', 'Лахтинско-Правобережная линиия'),
        ('ККЛ', 'Красносельско-Калининская линия'),
        ('Другое', 'Другое'),
    )
    line = models.CharField(max_length=50, choices=line_name, default='Другое', verbose_name="Объект строительства")
    
    # реквизиты банка в соответствии с объектом строительства (банком сопровождения)
    requisites = models.TextField(max_length=500, verbose_name="Реквизиты")
    
    """
    # государственный контракт
    gk = {
        "NVL_GK":line_name[0],
        "F2_GK":line_name[1],
        "LPL_GK":line_name[2],
        "KKL_GK":line_name[3],
    }
    """
    class Meta:
        ordering = ["line"] # сортировка объектов строительства по линии
        
    def __str__(self):
        """
        Возвращает название объекта строительства по линии (line)
        """
        return self.line