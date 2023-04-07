import pytest

from eshop_prices import EshopPrices, __version__


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
        assert e.headers == {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
        }

    def test_get_available_currencies(
        self, eshop_prices, eshop_prices_html, requests_mock
    ):
        requests_mock.get(eshop_prices.base_url, text=eshop_prices_html)
        assert eshop_prices.get_available_currencies() == {
            "": "Original currency",
            "ARS": "Argentine Peso – $",
            "AUD": "Australian Dollar – $",
            "BGN": "Bulgarian Lev – лв.",
            "CAD": "Canadian Dollar – $",
            "CHF": "Swiss Franc – CHF",
            "CLP": "Chilean Peso – $",
            "CNY": "Chinese Renminbi Yuan – ¥",
            "COP": "Colombian Peso – $",
            "CZK": "Czech Koruna – Kč",
            "DKK": "Danish Krone – kr.",
            "EUR": "Euro – €",
            "GBP": "British Pound – £",
            "GTQ": "Guatemalan Quetzal – Q",
            "HKD": "Hong Kong Dollar – $",
            "HRK": "Croatian Kuna – kn",
            "HUF": "Hungarian Forint – Ft",
            "IDR": "Indonesian Rupiah – Rp",
            "ILS": "Israeli New Sheqel – ₪",
            "INR": "Indian Rupee – ₹",
            "JPY": "Japanese Yen – ¥",
            "KRW": "South Korean Won – ₩",
            "MXN": "Mexican Peso – $",
            "MYR": "Malaysian Ringgit – RM",
            "NOK": "Norwegian Krone – kr",
            "NZD": "New Zealand Dollar – $",
            "PEN": "Peruvian Sol – S/",
            "PHP": "Philippine Peso – ₱",
            "PLN": "Polish Złoty – zł",
            "RON": "Romanian Leu – Lei",
            "RUB": "Russian Ruble – ₽",
            "SEK": "Swedish Krona – kr",
            "SGD": "Singapore Dollar – $",
            "THB": "Thai Baht – ฿",
            "TRY": "Turkish Lira – ₺",
            "TWD": "New Taiwan Dollar – $",
            "UAH": "Ukrainian Hryvnia – ₴",
            "USD": "United States Dollar – $",
            "VND": "Vietnamese Đồng – ₫",
            "ZAR": "South African Rand – R",
        }
