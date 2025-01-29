import pytest
from Balance import Account
from Balance import Bank


@pytest.fixture
def zero_balance_account():
    return Account()

@pytest.fixture
def bank_name():
    return "XYZ"



def test_deposit_into_empty_account(zero_balance_account):
    zero_balance_account    
    assert zero_balance_account.bank_deposit(50) == 50
    
    
def test_deposting_twise_empty_account():
    acc = Account()
    acc.bank_deposit(50)
    acc.bank_deposit(50)

    assert acc.balance == 100 


def test_Bank(zero_balance_account, bank_name):

    assert bank_name == "XYZ"
    assert zero_balance_account.bank_deposit(50) == 50
