import pytest

from eshop_prices import EshopPrices


@pytest.fixture
def eshop_prices():
    return EshopPrices()


@pytest.fixture
def eshop_prices_html():
    with open("tests/fixtures/eshop_prices.html", "r") as f:
        return f.read()
