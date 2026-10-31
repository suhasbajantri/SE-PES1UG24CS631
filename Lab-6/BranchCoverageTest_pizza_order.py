import pytest
from pizza_order import pizza_price, order_discount, delivery_status


# Pizza price branches

def test_invalid_pizza_size():
    with pytest.raises(ValueError):
        pizza_price("extra_large", 1, False)


def test_negative_toppings():
    with pytest.raises(ValueError):
        pizza_price("medium", -1, False)


def test_three_or_less_toppings():
    assert pizza_price("medium", 3, False) == 470


def test_more_than_three_toppings():
    assert pizza_price("medium", 5, False) == 530


def test_cheese_burst_small():
    with pytest.raises(ValueError):
        pizza_price("small", 1, True)


def test_cheese_burst_available():
    assert pizza_price("large", 1, True) == 640


def test_no_cheese_burst():
    assert pizza_price("large", 0, False) == 500


# Order discount branches

def test_order_below_300():
    assert order_discount(250, "monday", False) == 0


def test_tuesday_discount():
    assert order_discount(400, "tuesday", False) == 200


def test_weekend_discount():
    assert order_discount(500, "saturday", False) == 0


def test_normal_day_discount():
    assert order_discount(500, "monday", False) == 50


def test_student_discount():
    assert order_discount(500, "monday", True) == 100


# Delivery branches

def test_distance_more_than_10():
    assert delivery_status(20, 15) == "not deliverable"


def test_on_time():
    assert delivery_status(30, 5) == "on time"


def test_late():
    assert delivery_status(40, 5) == "late"


def test_free_pizza():
    assert delivery_status(50, 5) == "free pizza"