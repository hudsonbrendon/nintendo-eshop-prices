import urllib

import bs4
import cchardet
import lxml
import requests


class EshopPrices:
    def __init__(self, currency=""):
        self.base_url = "https://eshop-prices.com/"

        self.currency = currency

    def __parse_games_list_item(
        self, games_list_item: bs4.element.Tag
    ) -> dict:
        game_title = games_list_item.find_all("h5")[0].string
        game_url = games_list_item["href"]
        for i, s in enumerate(
            games_list_item.find_all("span", {"class": "price-tag"})[0].strings
        ):
            print(i, s)
        try:
            game_price = list(
                games_list_item.find_all("span", {"class": "price-tag"})[
                    0
                ].strings
            )[2].strip()
        except IndexError:
            game_price = list(
                games_list_item.find_all("span", {"class": "price-tag"})[
                    0
                ].strings
            )[0].strip()

        return {
            "game_title": game_title,
            "game_uri": game_url,
            "game_price": game_price,
        }

    def __parse_country_column(self, country_column: bs4.element.Tag) -> str:
        try:
            return list(country_column.strings)[3].strip()
        except IndexError:
            return list(country_column.strings)[0].strip()

    def __parse_price_column(self, price_column: bs4.element.Tag) -> str:
        try:
            original_price = price_column.div.find("del").string.strip()
            discounted_price = list(price_column.div.strings)[2].strip()
            return {
                "current_price": discounted_price,
                "original_price": original_price,
                "discount": True,
            }
        except AttributeError:
            original_price = price_column.string.strip()
            return {
                "current_price": original_price,
                "original_price": original_price,
                "discount": False,
            }

    def __parse_prices_table_row(self, row):
        columns = row.find_all("td")

        country = self.__parse_country_column(columns[1])
        try:
            meta = columns[2].span["title"]
        except TypeError:
            meta = None
        price = self.__parse_price_column(columns[3])

        return {"country": country, "meta": meta, "price": price}

    def get_prices_from_url(self, game_url: str) -> [{str: str}]:
        request_url = (
            self.base_url + game_url
        )  # + f'?currency={self.currency}'
        print("Making request to " + request_url)

        response = requests.get(
            request_url,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
            },
        )

        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, "lxml")

            prices_table = soup.find_all("table", {"class": "prices-table"})[0]

            prices = []
            for row in prices_table.tbody.find_all("tr"):
                # columns = row.find_all('td')
                try:
                    prices.append(self.__parse_prices_table_row(row))
                except IndexError as e:
                    print(e, row)

            return prices
        else:
            return f"Error getting prices from game_url! (Status = {response.status_code})"

    def search(self, query: str) -> {str: str}:
        encoded_query = urllib.parse.quote(query, safe="")

        request_url = (
            self.base_url + f"games?q={encoded_query}&currency={self.currency}"
        )

        response = requests.get(
            request_url,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
            },
        )

        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, "lxml")

            games_list = soup.find_all("a", {"class": "games-list-item"})

            results = {}

            for games_list_item in games_list:
                games_list_item = self.__parse_games_list_item(games_list_item)
                results[games_list_item["game_title"]] = {
                    "best_price": games_list_item["game_price"],
                    "uri": games_list_item["game_uri"],
                }

            return results
        else:
            return (
                f"Error performing search! (Status = {response.status_code})"
            )
        pass

    def get_prices(self, game: str) -> [{str: str}]:
        search_results = self.search(game)

        if len(search_results) == 0:
            pass
        elif len(search_results) == 1:
            return self.get_prices_from_url(list(search_results.values())[0])
        else:
            print("More than one game found from that query:")
            for i, game_title in enumerate(search_results.keys()):
                print(f"{i} - {game_title}")

            game_to_get = input(
                "What game do you want the prices for (use the number) ? "
            )

            return self.get_prices_from_url(
                list(search_results.values())[int(game_to_get)]["uri"]
            )

    def get_top_discounts(self) -> [{str: str}]:
        request_url = (
            self.base_url
            + f"games/on-sale?direction=desc&sort_by=discount&currency={self.currency}"
        )

        response = requests.get(
            request_url,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
            },
        )

        soup = bs4.BeautifulSoup(response.text, "lxml")

        games_list = soup.find_all("a", {"class": "games-list-item"})

        results = {}

        for games_list_item in games_list:
            games_list_item = self.__parse_games_list_item(games_list_item)
            results[games_list_item["game_title"]] = {
                "best_price": games_list_item["game_price"],
                "uri": games_list_item["game_uri"],
            }

        return results

    def get_available_currencies(self) -> {str: str}:
        response = requests.get(
            self.base_url,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
            },
        )

        soup = bs4.BeautifulSoup(response.text, "lxml")
        currency_select = soup.find_all("select", {"name": "language-select"})[
            0
        ]
        options = currency_select.find_all("option")

        result = {}
        for option in options:
            result[option["value"]] = option.string

        return result