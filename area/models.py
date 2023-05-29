from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Person(models.Model):
    owner = models.OneToOneField(User,
                            unique=True,
                            max_length=100,
                            on_delete=models.CASCADE,
                            related_name='person',
                            blank=True,
                            )
    name = models.CharField('Имя', max_length=100, null=True)
    surname =  models.CharField('Фамилия', max_length=100, null=True)
    second_name = models.CharField('Отчество', max_length=100, null=True)
    balance = models.DecimalField('Баланс', max_digits=10, decimal_places=2)
    personal_num = models.DecimalField('Персональный счет', max_digits=10, decimal_places=0)
    number = models.DecimalField('Номер телефона', max_digits=15, decimal_places=0)
    tariff_start = models.DecimalField('Начала тарифа', max_digits=10, decimal_places=2)
    tariff_end = models.DecimalField('Конец тарифа', max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.owner.email} Σ(°△°|||)' 