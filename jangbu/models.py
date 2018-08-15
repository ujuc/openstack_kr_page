from django.db import models
from django.utils import timezone

from openstack_kr.models import TimeStampedModel


class Accounts(TimeStampedModel):
    add_date = models.DateField(default=timezone.localdate)
    # 지출
    expenditure = models.BigIntegerField(default=0)
    # 수익
    revenue = models.BigIntegerField(default=0)
    # 영수증
    receipt = models.TextField()
    # 지급 여부
    payment = models.BooleanField(default=False)
    note = models.TextField()
