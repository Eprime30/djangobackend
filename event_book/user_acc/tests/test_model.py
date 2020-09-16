import pytest

import factory

from ..factories import AccountFactory


@pytest.mark.django_db
def test_account_create(account):
    account = account

    assert account.email == f'{account.first_name}.{account.last_name}@gmail.com'.lower()
    assert account.get_first_name() == account.first_name
    assert account.get_fullname(
    ) == f'{account.last_name} {account.first_name}'
    assert account.email_user('Hey you', 'Hello Iyanu') == 1
