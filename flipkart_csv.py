"""Weather Scrap Data CSV Update"""

import os
from csv import writer, reader

from constant import CSV_PATH, CSV_NOT_FOUND, CSV_ROWS
from utils import CsvFileNotExists


class CsvScrap:
    """class to implement csv logic for scraping"""

    def __init__(self):
        if not os.path.isfile(CSV_PATH):
            with open("flipkart_products.csv", "a") as fp:
                write_obj = writer(fp)
                write_obj.writerow(CSV_ROWS)

    @staticmethod
    def insert_into_csv(flipkart_data: dict) -> None:
        """
        static method just to write a CSV File
        @param flipkart_data: dict
        @return:None
        """
        if os.path.isfile(CSV_PATH):
            with open("flipkart_products.csv", "a") as fp:
                data = flipkart_data.values()
                write_obj = writer(fp)
                write_obj.writerow(data)
            print("Data Inserted: ", data)
        else:
            raise CsvFileNotExists(CSV_NOT_FOUND)

    @staticmethod
    def read_csv() -> None:
        """
        static method just to read a CSV File
        @return:None
        """
        if os.path.isfile(CSV_PATH):
            with open("flipkart_products.csv", "r") as fp:
                read = reader(fp)
                for row in read:
                    print(row)
        else:
            raise CsvFileNotExists(CSV_NOT_FOUND)


if __name__ == "__main__":
    obj = CsvScrap()
    obj.read_csv()
