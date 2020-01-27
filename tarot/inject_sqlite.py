"""
WARNING: This script will DELETE all records of the spesified table before injections

This script uses source data from previously generated csv file as well as a images folder
provided via command line arguments, to first DELETE all records of specified table before
INSERT new records obtained from the aforementioned csv, it proceeds to inject binary
image data from each image of the images folder into the spesified database,table,field
as per command line arguments
    database: 'name of database file'
    table 'name of table'
    filed 'name of field to inject image'
    images 'folder containing images to be injected'
"""
import sqlite3
import pandas
import argparse
from pathlib import Path


class TarotDatabaseConnection(object):
    def __init__(self, database):
        self.connection = None
        self.cursor = None
        self.database = database

    def __enter__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, *exc):
        self.connection.close()


if __name__ == "__main__":
    CSV_SRC = 'generators_generator.csv'
    data = pandas.read_csv(CSV_SRC)
    parser = argparse.ArgumentParser(
        description="Script to inject images into sqlite3 database field, in additon to csv data"
    )
    parser.add_argument("database", help="sqlite3 database file")
    parser.add_argument("table", help="sqlite3 table name")
    parser.add_argument("field", help="filed to inject the images")
    parser.add_argument("images", help="folder containing images")
    arguments = parser.parse_args()
    database = arguments.database
    table_name = arguments.table
    field = arguments.field
    image_dir = arguments.images

    with TarotDatabaseConnection(database) as db:
        # drop existing records from table
        db.cursor.execute(f"DELETE FROM {table_name}",)
        db.connection.commit()
