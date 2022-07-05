import sqlite3
from SQLite3Module.SQLite3_DBType import *
from typing import List, Dict, Any


class Table:
    def __init__(self, name: str, cursor: sqlite3.Cursor, connector: sqlite3.Connection):
        self.__name = name
        self.__cursor = cursor
        self.__connector = connector
        self.__primary_key = None
        self.__table_labels = None
        self.__is_loaded = False

    def __nonzero__(self) -> bool:
        return self.__is_loaded

    @property
    def column_names(self) -> List[str]:
        """
        This property returns a list of column names
        """
        if not self.__is_loaded:
            raise Exception(f"DataBase \'{self.__name}\' is not exist!. Try using \'Table.create_table\'.")
        return list(self.__table_labels.keys())

    def create_table(self, labels: Dict[str, DBType], primary_key: str = None) -> None:
        """
        This method creates a table with the specified columns. If "primary_key" is not specified, then the first
        column will be considered the identifier, otherwise - the one selected by the user.
        :param labels: A dictionary where the key is the column name and the value is the data type
        :param primary_key: The column that will be considered the key
        """
        if self.__is_loaded:
            raise Exception("DataBase is already exist!")
        if primary_key is not None:
            if primary_key not in labels:
                raise Exception(f"Column \'{primary_key}\' not exist in table labels!")
            self.__primary_key = primary_key
        else:
            self.__primary_key = list(labels.keys())[0]
        self.__cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.__name} ({Table.__prep_labels(labels)})")
        self.__connector.commit()
        self.__table_labels = labels
        self.__is_loaded = True

    def get_from_cell(self, key: str, column_name: str) -> Any:
        """
        This method returns the value from the cell located in the column "column_name" and the row with the
         identifier "key"
        :param key: Unique identifier
        :param column_name: The name of the column from which the value should be returned
        """
        if not self.__is_loaded:
            raise Exception(f"DataBase \'{self.__name}\' is not exist!. Try using \'Table.create_table\'.")
        if column_name not in self.__table_labels:
            raise Exception(f"Column \'{column_name}\' not exist in table labels!")
        self.__cursor.execute(f"SELECT {column_name} FROM {self.__name} WHERE {self.__primary_key} = '{key}'")
        return self.__cursor.fetchone()[0]

    def set_to_cell(self, key: str, column_name: str, new_value: Any, commit: bool = True) -> None:
        """
        Этот метод записывает значение new_value в колонку column_name в строку с идентификатором key
        :param key: Unique identifier
        :param column_name: Column name
        :param new_value: The value we want to write
        :param commit: Is it worth committing (often a commit is needed 1 time in 10-100 operations)
        """
        if not self.__is_loaded:
            raise Exception(f"DataBase \'{self.__name}\' is not exist!. Try using \'Table.create_table\'.")
        if column_name not in self.__table_labels:
            raise Exception(f"Column \'{column_name}\' not exist in table labels!")
        self.__cursor.execute(f"UPDATE {self.__name} SET {column_name} = '{new_value}' WHERE {self.__primary_key} = '{key}'")
        if commit:
            self.__connector.commit()

    def add_row(self, row: list, commit: bool = True) -> None:
        """
        This method adds a new row to the table
        :param row: List of row values
        :param commit: Is it worth committing (often a commit is needed 1 time in 10-100 operations)
        """
        if not self.__is_loaded:
            raise Exception(f"DataBase \'{self.__name}\' is not exist!. Try using \'Table.create_table\'.")
        if len(row) != len(self.__table_labels):
            raise Exception(f"There are only {len(self.__table_labels)} columns in the database "
                            f"\'{self.__name}\', and you are trying to write {len(row)}")
        values = ", ".join(["'" + str(i) + "'" for i in row])
        self.__cursor.execute(f"INSERT INTO {self.__name} VALUES ({values})")
        if commit:
            self.__connector.commit()

    def get_row(self, key: str) -> Dict[str, Any]:
        """
        This method gets values from all columns of the "row" table
        :param key: Unique identifier
        """
        if not self.__is_loaded:
            raise Exception(f"DataBase \'{self.__name}\' is not exist!. Try using \'Table.create_table\'.")
        self.__cursor.execute(f"SELECT * FROM {self.__name} WHERE {self.__primary_key} = '{key}'")
        request = self.__cursor.fetchall()
        if len(request) == 0:
            raise Exception("There are no values for this query!")
        if len(request[0]) != len(self.column_names):
            raise Exception("The number of columns and values does not match!"
                            f"{len(self.column_names)} columns and {len(request[0])} values were detected!")
        return {column: value for column, value in zip(self.column_names, request[0])}

    def delete_row(self, key: str) -> None:
        """
        This method removes the "row" from the table
        :param key: Unique identifier
        """
        if not self.__is_loaded:
            raise Exception(f"DataBase \'{self.__name}\' is not exist!. Try using \'Table.create_table\'.")
        self.__cursor.execute(f"DELETE FROM {self.__name} WHERE {self.__primary_key} = '{key}'")
        self.__connector.commit()

    def get_column(self, column_name: str) -> List[Any]:
        """
        This method returns all values from the "column_name" column
        :param column_name: Column name
        """
        if not self.__is_loaded:
            raise Exception(f"DataBase \'{self.__name}\' is not exist!. Try using \'Table.create_table\'.")
        if column_name not in self.__table_labels:
            raise Exception(f"Column \'{column_name}\' not exist in table labels!")
        self.__cursor.execute(f"SELECT {column_name} FROM {self.__name}")
        return [sfa[0] for sfa in self.__cursor.fetchall()]

    def get_all_keys(self) -> List[Any]:
        """
        This method returns all values of all identifiers (a column whose values are unique for each row)
        """
        if not self.__is_loaded:
            raise Exception(f"DataBase \'{self.__name}\' is not exist!. Try using \'Table.create_table\'.")
        self.__cursor.execute(f"SELECT {self.__primary_key} FROM {self.__name}")
        return [sfa[0] for sfa in self.__cursor.fetchall()]

    def commit(self) -> None:
        """
        Confirms the entry in the table
        """
        self.__connector.commit()

    @staticmethod
    def __prep_labels(labels: Dict[str, DBType]) -> str:
        """
        This method converts a custom dictionary with columns and their types into a SQL-friendly part of the command
        :param labels:A dictionary where the key is the column name and the values are the data type from the DBType set
        :return: The finished part of the string
        """
        return ",".join([f"{label} {labels[label].value}" for label in labels])
