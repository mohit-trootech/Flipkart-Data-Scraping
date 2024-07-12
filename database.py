"""Database File to Store Scrapped Data"""

from sqlite3 import connect, ProgrammingError, OperationalError

from constant import DB, SQL_EXECUTION_ERROR, CREATE_TABLE, INSERT_2_TABLE, DB_OK
from utils import SqlExecutionError


class FlipkartDatabase:
    """Flipkart Database to Handle Data"""

    def __init__(self):
        """Constructor for FlipkartDatabase.__main__ class"""
        self.db = connect(DB)
        self.cursor = self.db.cursor()
        self.create_flipkart_table()

    def create_flipkart_table(self) -> None:
        """
        method to create table for Storing the Weather Data
        @return: None
        """
        try:
            self.cursor.execute(CREATE_TABLE)
            self.db.commit()
        except (ProgrammingError, OperationalError) as sql_error:
            print(SqlExecutionError(SQL_EXECUTION_ERROR.format(err=sql_error)))
            return

    def insert_into_flipkart_table(self, flipkart_products: dict) -> None:
        """
        insert Flipkart data into database
        @param flipkart_products: dict
        @return: None
        """
        try:
            self.cursor.execute(INSERT_2_TABLE, flipkart_products)
            self.db.commit()
            print(DB_OK)
        except (ProgrammingError, OperationalError) as sql_error:
            print(SqlExecutionError(SQL_EXECUTION_ERROR.format(err=sql_error)))
            return


if __name__ == "__main__":
    obj = FlipkartDatabase()
