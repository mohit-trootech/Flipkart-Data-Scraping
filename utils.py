"""Scrapping Utilities: geturl, get error message, etc"""

import re

from constant import URL


class CsvFileNotExists(BaseException):
    """Custom class for CSV File Not Found"""

    def __init__(self, msg):
        super(CsvFileNotExists, self).__init__(msg)


class SqlExecutionError(BaseException):
    """Custom class for SQL Exception"""

    def __init__(self, msg):
        super(SqlExecutionError, self).__init__(msg)


class RequestError(BaseException):
    """custom class for all request status code error other than 200"""

    def __init__(self, msg):
        super(RequestError, self).__init__(msg)


class Bs4Error(BaseException):
    """custom bs4 Exception class"""

    def __init__(self, msg):
        super(Bs4Error, self).__init__(msg)


def get_request_url(address: str) -> str:
    """
    get Request URL City
    @param address: str
    @return: str
    """
    print(URL.format(address=address))
    return URL.format(address=address)


def clean_format_data(title: str, data: str) -> dict:
    """
    function to clean and get required data from scrapped data and create dictionary from it
    @param title:str
    @param data:str
    @return:dict
    """
    weather_data = {}
    amounts = []
    for item in data.split(" "):
        item = re.sub(r"\.", "", item)
        if item.isnumeric():
            amounts.append(int(item))
    weather_data.setdefault("name", title)
    amounts = amounts[-1:-5:-1]
    weather_data.update(
        {
            "price": amounts[-2],
            "average": amounts[-3],
            "lowest": amounts[-4],
            "highest": amounts[-1],
            "description": data,
        }
    )
    return weather_data


def get_flipkart_product_code(url):
    return url.split("/")[3]


if __name__ == "__main__":
    pass
