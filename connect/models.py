from django.db import models

class Order(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    email = models.EmailField('Email' , max_length=50)
    number = models.DecimalField('Описания продукта ',max_digits=10, decimal_places=0)
    address = models.CharField('Адрес', max_length=100)

    def __str__(self):
        return f' {self.title} ^_^'