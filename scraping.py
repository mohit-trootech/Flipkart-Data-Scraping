"""File to Implement Scraping data Class"""

from bs4 import BeautifulSoup

from constant import BS4_ERROR, CSV_OK
from database import FlipkartDatabase
from flipkart_csv import CsvScrap
from utils import clean_format_data, Bs4Error


class DataScrap(FlipkartDatabase):
    """DataScrap Class to Implement Scraping Inherits FlipkartDatabase to Access Database"""

    def __init__(self, page) -> None:
        """
        Constructor for DataScrap.__main__ class
        @param address: str
        @param page: any
        """
        super().__init__()
        self.page = page
        self.flipkart_data = None
        self.flipkart_csv = CsvScrap()

    def scrap_filter_data(self) -> dict:
        """
        as the name suggest main method to implement data scraping and cleaning using utils and find.
        @return: dict
        """
        soup = BeautifulSoup(self.page.content, "html5lib")
        title = soup.find("h1", {"class": "font-semibold text-lg"}).text
        amounts = soup.find("div", {"class": "content-width mx-auto px-3"}).text
        if title and amounts:
            self.flipkart_data = clean_format_data(title, amounts)
            print(self.flipkart_data)
            self.create_database_entry_of_scrap_data()
        else:
            raise Bs4Error(BS4_ERROR)

    def create_database_entry_of_scrap_data(self):
        self.insert_into_flipkart_table(self.flipkart_data)

    def csv_handling(self, read: bool = False) -> None:
        """
        method to handle csv write and read operations
        @param: read: bool
        @return: None
        """
        self.flipkart_csv.insert_into_csv(self.flipkart_data)
        print(CSV_OK)
        if read:
            self.flipkart_csv.read_csv()
