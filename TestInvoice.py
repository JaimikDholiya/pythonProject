import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Cricket_Boll': {'qnt': 15, 'unit_price': 2.5, 'discount': 10},
                'Tennis_Ball': {'qnt': 10, 'unit_price': 3.5, 'discount': 5}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalucateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38
