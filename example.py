import os
from SQLite3Module.SQLite3_base import *

my_sqlite3_database = DataBase(path=os.getcwd(), filename="my_BD.sqlite3")  # Creating (or connection) DataBase
my_sqlite3_database.add_table(tablename="my_first_table",  # Setting name of table
                              columns={"user_id": DBType.INTEGER,
                                       "firstname": DBType.TEXT,
                                       "lastname": DBType.TEXT,
                                       "real value": DBType.REAL})

my_sqlite3_database.add_table(tablename="my_second_table",  # Yes, we can creating one more table
                              columns={"user_id": DBType.INTEGER,
                                       "firstname": DBType.TEXT,
                                       "lastname": DBType.TEXT,
                                       "real value": DBType.REAL},
                              primary_key="real value")

# my_sqlite3_database.delete_table(table_name="my_first_table") # If we want to delete table

print(my_sqlite3_database.get_table("my_second_table"))  # I


