from django.db import models
from django.conf import settings
from mainapp.models import Deal


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket')
    deal = models.ForeignKey(Deal,
                                      on_delete=models.CASCADE)
    shifts = models.PositiveIntegerField(verbose_name='кол-во смен',
                                         default=0)
    add_datetime = models.DateTimeField(verbose_name='время',
                                        auto_now_add=True)


    @property
    def deal_cost(self):
        return self.deal.price * self.shifts

    @property
    def total_shifts(self):
        _deal = Basket.objects.filter(user=self.user)
        _total_shifts = sum(list(map(lambda x: x.shifts, _deal)))
        return _total_shifts

    @property
    def total_cost(self):
        _deal = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.deal_cost,
                                   _deal)))
        return _total_cost

    @staticmethod
    def get_items(user):
        return user.basket.select_related().order_by(
            'deal__country')
