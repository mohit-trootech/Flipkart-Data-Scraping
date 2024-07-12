"""Constant Variables"""

import os

BASE_DIR = os.getcwd()


# Required
URL = "https://pricehistoryapp.com/product/{address}"
DB = "flipkart_products.db"
STATUS_CODE_OK = 200
CSV_PATH = os.path.join(BASE_DIR, "flipkart_products.csv")
DB_OK = "Data Insertion Completed Check Database Table"
CSV_OK = "Data Insertion Completed in CSV"
CSV_ROWS = (
    "name",
    "price",
    "average",
    "lowest",
    "highest",
    "description",
)
# Errors
STATUS_CODE_ERROR = "Not Able to Fetch URL Return with Status Code: {status_code}"
SQL_EXECUTION_ERROR = "SQL Execution Failed Check Status: {err}"
BS4_ERROR = "Unable to Find Required Data Please Try Again or Check the Implementation"
CSV_NOT_FOUND = "Request CSV Not Found"


# SQL Execution
CREATE_TABLE = (
    "CREATE TABLE IF NOT EXISTS flipkart_data (id INTEGER PRIMARY KEY, name VARCHAR(128), price INT, "
    "average INT, lowest INT, highest INT, description VARCHAR(9999));"
)


INSERT_2_TABLE = (
    "INSERT INTO flipkart_data (name, price, average, lowest, highest, description) VALUES (:name, "
    ":price , :average, :lowest, :highest, :description);"
)

# Require Data in This Format For Reference
# motorola-edge-50-pro-5g-with-68w-charger-luxe-lavender-256-gb
# motorola-g34-5g-ocean-green-128-gb-109b
# vivo-t3-lite-5g-majestic-black-128-gb
