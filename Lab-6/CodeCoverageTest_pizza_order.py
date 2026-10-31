import pytest
from pizza_order import pizza_price, order_discount, delivery_status


def test_medium_plain_pizza():
    assert pizza_price("medium", 0, False) == 350


def test_large_many_toppings():
    assert pizza_price("large", 5, False) == 680


def test_invalid_size():
    with pytest.raises(ValueError):
        pizza_price("extra_large", 2, False)


def test_invalid_toppings():
    with pytest.raises(ValueError):
        pizza_price("medium", -1, False)


def test_cheese_burst_small_not_available():
    with pytest.raises(ValueError):
        pizza_price("small", 1, True)


def test_cheese_burst_medium():
    assert pizza_price("medium", 2, True) == 530


def test_order_below_300():
    assert order_discount(250, "monday", False) == 0


def test_tuesday_discount():
    assert order_discount(400, "tuesday", False) == 200


def test_weekend_discount():
    assert order_discount(500, "saturday", False) == 0


def test_normal_day_student_discount():
    assert order_discount(500, "monday", True) == 100


def test_on_time_delivery():
    assert delivery_status(30, 5) == "on time"


def test_late_delivery():
    assert delivery_status(40, 5) == "late"


def test_free_pizza_delivery():
    assert delivery_status(50, 5) == "free pizza"


def test_not_deliverable():
    assert delivery_status(20, 15) == "not deliverable"