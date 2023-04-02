# Nintendo Eshop Prices

A wrapper python for [eshop-prices.com](https://eshop-prices.com/)

![image](https://user-images.githubusercontent.com/5201888/229378038-9fc6fc8c-bb52-4b94-82d1-620e0cfc333b.png)

# Available resources

- [x] Search
- [x] Get prices from URL
- [x] Get prices
- [x] Get top discounts
- [x] Get availables currencies

# Install

```bash
$ pip install eshop-prices
```

# Contribute

Clone the repository project:

```bash
$ git clone https://github.com/hudsonbrendon/eshop-prices.git
```

Make sure [Poetry](https://python-poetry.org/) is installed, otherwise:

```bash
$ pip install -U poetry
```

Install the dependencies:

```bash
$ poetry install
```

To run the tests:

```bash
$ pytest
```

# Usage

## Search

```python
from eshop_prices import EshopPrices

eshop = EshopPrices(currency="BRL")
eshop.search("Zelda")
```

## Get prices from url

```python
from eshop_prices import EshopPrices

eshop = EshopPrices(currency="BRL")
eshop.get_prices_from_url("/games/164-mario-kart-8-deluxe/")
```

## Get prices

```python
from eshop_prices import EshopPrices

eshop = EshopPrices(currency="BRL")
eshop.get_prices("Zelda")
```

## Get top discounts

```python
from eshop_prices import EshopPrices

eshop = EshopPrices(currency="BRL")
eshop.get_top_discounts()
```

## Get available currencies

```python
from eshop_prices import EshopPrices

eshop = EshopPrices(currency="BRL")
eshop.get_available_currencies()
```

# Dependencies

- [Python >=3.8](https://www.python.org/downloads/release/python-388/)

# License

[MIT](http://en.wikipedia.org/wiki/MIT_License)
