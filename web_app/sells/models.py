from django.db import models
from django.contrib.auth.models import  User

class Sell(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    date = models.DateField(null=True, blank=True)
    summ = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    price_for_one = models.FloatField(null=True, blank=True)
    full_price = models.FloatField(null=True, blank=True)
    margue = models.FloatField(null=True, blank=True)





    DONE = 'DONE'
    WAITING = 'WAITING'
    DELIVERY_PAY = "DELIVERY_PAY"
    NO_STATUS = 'NOSTATUS'

    STATUS_CHOICES = {
        DONE: 'Оплачено',
        WAITING: 'Ожидает оплаты',
        DELIVERY_PAY:  'Наложенный платеж',
        NO_STATUS: 'Информация отсутствует',
    }

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NO_STATUS,
    )

    def __str__(self):
        if self.name == None:
            return 'Без названия'
        else:
            return 'Продажа - ' + self.name + ' Статус: ' + self.status


