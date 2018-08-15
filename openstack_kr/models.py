"""
공통으로 사용하는 것들을 넣어두자.
"""
from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    'created', 'modified' 필드를 자동으로 입력해준다.
    """
    created = models.DateTimeField(default=timezone.now, auto_created=True)
    modified = models.DateTimeField(default=timezone.now, auto_created=True)

    class Meta:
        abstract = True
