"""
공통으로 사용하는 것들을 넣어두자.
"""
from django.db import models


class TimeStampedModel(models.Model):
    """
    'created', 'modified' 필드를 자동으로 입력해준다.
    """
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_created=True)

    class Meta:
        abstract = True
