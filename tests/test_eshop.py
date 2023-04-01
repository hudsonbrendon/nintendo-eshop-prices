import pytest

from eshop_prices import EshopPrices, __version__


@pytest.fixture
def eshop_prices():
    return EshopPrices()


def test_version():
    assert __version__ == "0.1.0"


class TestEshopPrices:
    def test_init(self, eshop_prices):
        assert eshop_prices.currency == ""

        e = EshopPrices("USD")
        assert e.currency == "USD"

    def test_base_url(self, eshop_prices):
        assert eshop_prices.base_url == "https://eshop-prices.com/"

    def test_currency(self, eshop_prices):
        assert eshop_prices.currency == ""

        e = EshopPrices("USD")
        assert e.currency == "USD"

    def test_headers(self, eshop_prices):
        assert eshop_prices.currency == ""

        e = EshopPrices("USD")
        assert e.headers == {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"}
