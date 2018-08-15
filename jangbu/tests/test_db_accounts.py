from jangbu.models import Accounts

import pytest


@pytest.mark.django_db
def test_save():
    first_save = Accounts(
        expenditure=20000, receipt='https://openstack.org',
        payment=True, note='TTTest'
    )
    first_save.save()
    assert first_save.expenditure == 20000
    assert first_save.payment is True
    assert first_save.receipt == 'https://openstack.org'
