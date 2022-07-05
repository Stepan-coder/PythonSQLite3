import os
import sqlite3
from typing import List, Dict, Any
from SQLite3Module.SQLite3_table import *
from SQLite3Module.SQLite3_DBType import *


class DataBase:
    def __init__(self, path: str, filename: str):
        """
        This method initializes the main class to operate (and manage) the database
        :param path: The path where the database is located (it is necessary to locate the database)
        :param filename: The name of the database (along with the extension). For example: 'some.bd'
        """
        self.__tables = {}
        self.__path = DataBase.__is_path_valid(path=path)
        self.__filename = DataBase.__is_filename_valid(filename=filename)
        self.__create_cursor(path_to_file=os.path.join(self.__path, self.__filename))

    def __len__(self):
        return len(self.__tables)

    @property
    def cursor(self) -> sqlite3.Cursor:
        """
        This property returns the cursor for the database (directly the thing that works with database cells)
        """
        return self.__cursor

    @property
    def connector(self) -> sqlite3.Connection:
        """
        This property returns the connector for the database
        (the thing through which the connection to the database is established)
        """
        return self.__connector

    def create_table(self, name: str, labels: Dict[str, DBType], primary_key: str = None) -> None:
        """
        This method creates a table in the database
        :param name: Table name
        :param labels: A dictionary where the key is the column name and the value is the data type
        :param primary_key: Key column
        """
        table = Table(name=name,
                      cursor=self.__cursor,
                      connector=self.__connector)
        table.create_table(labels=labels, primary_key=primary_key)
        self.__tables[name] = table

    def get_table(self, table_name: str) -> Table:
        """
        We get the "Table" object for further interaction with it.
        :param table_name: Table name
        """
        if table_name not in self.__tables:
            raise Exception(f"Table \'{table_name}\' not exist in DataBase!")
        return self.__tables[table_name]

    def __create_cursor(self, path_to_file: str) -> None:
        """
        This method creates a cursor (entity, to interact with the database)
        :param path_to_file: The path to the database, right along with the file. For example: *\some.db
        """
        self.__connector = sqlite3.connect(path_to_file, check_same_thread=False)
        self.__cursor = self.__connector.cursor()

    @staticmethod
    def __is_path_valid(path: str) -> str:
        """
        This method checks if this string is the path to the folder/file
        :param path: The intended path to the file
        """
        if os.path.exists(path):
            return path
        else:
            raise Exception(f"The path \'{path}\' is not valid!")

    @staticmethod
    def __is_filename_valid(filename: str) -> str:
        """
        This method checks if this string is the path to the folder/file
        :param filename: The intended path to the file
        """
        if filename.endswith(".db"):
            return filename
        else:
            raise Exception(f"The filename \'{filename}\' is not valid!")