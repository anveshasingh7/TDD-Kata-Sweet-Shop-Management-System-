
import pytest
from model.sweet import Sweet
from service.inventory import Inventory
from service.sweetshop_service import SweetShopService


@pytest.fixture
def svc():
    inv = Inventory()
    shop = SweetShopService(inv)
    shop.add_sweet(Sweet("s1", "Ladoo", 10.0, 5))
    shop.add_sweet(Sweet("s2", "Barfi", 15.0, 2))
    return shop


def test_create_order_success(svc):
    order = svc.create_order("o1", {"s1": 2, "s2": 1})
    assert order.items["s1"] == 2
    assert svc.inventory.get_sweet("s1").stock == 3


def test_create_order_insufficient_stock(svc):
    with pytest.raises(Exception):
        svc.create_order("o2", {"s2": 3})



    svc.create_order("o3", {"s1": 2})
    svc.cancel_order("o3")
    assert svc.inventory.get_sweet("s1").stock == 5
    assert svc.get_order("o3").status == "CANCELLED"
