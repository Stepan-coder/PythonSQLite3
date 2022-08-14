import os
from SQLite3Module.SQLite3_base import *


# To work with SQLite3Module, it is enough to simply import it into your project,
# the main file is SQLite3Module/SQLite3_base.py .
my_sqlite3_database = DataBase(path=os.getcwd(), filename="my_BD.sqlite3")

# Now you don't need to know the SQL language to create a table, just call the appropriate method and pass the
# appropriate parameters to it. In this concrete case, the unique key primary_key will be the column `user_id'.
my_sqlite3_database.add_table(tablename="users",
                              columns={"user_id": DBType.INTEGER,
                                       "firstname": DBType.TEXT,
                                       "lastname": DBType.TEXT,
                                       "score": DBType.REAL})

# Yes, we can creating one more table :) To change the primary_key, when initializing the table,
# you need to explicitly specify the column that you want to make the main one. For example, like this:
my_sqlite3_database.add_table(tablename="products",
                              columns={"product_id": DBType.INTEGER,
                                       "name": DBType.TEXT,
                                       "description": DBType.TEXT},
                              primary_key="product_id")

my_sqlite3_database.add_table(tablename="deals",
                              columns={"deal_id": DBType.INTEGER,
                                       "user_id": DBType.INTEGER,
                                       "product_id": DBType.INTEGER},
                              primary_key="deal_id")


# Naturally, what can be created can be deleted. Deleting a table is not a cancellable action!!!
# my_sqlite3_database.delete_table(table_name="users")
# my_sqlite3_database.delete_table(table_name="users")

# To see which tables the database consists of and in what state they are now, you can run the following code.
print(my_sqlite3_database)

# So, the database is ready, only the table with users should be returned back (otherwise it doesn't work out well))
# I'll just recreate the database and comment on deleting the "users" table
# To add a new entry to the table, you need to do 2 things, understand what and to which table we add)))
# The `add_row` method accepts a dictionary, where the key is the column name, and the value is the value
# that needs to be written to this column.
my_sqlite3_database.get_table("users").add_row(row={"user_id": 1,
                                                    "firstname": "Ivan",
                                                    "lastname": "Ivanov",
                                                    "score": 3.14159})

# Now we can try to get this string from the database and see what will be returned to us. The `key` parameter
# corresponds to a string with such a unique identifier as `key` (primary_key, which we specified earlier)
print(my_sqlite3_database.get_table("users").get_row(key="1"))

# Similarly to records, we can delete the row we need from the table as follows:
my_sqlite3_database.get_table("users").delete_row(key="1")

# With individual cells, you can do all the same actions: overwriting and receiving. Looking)
# Deletion is not possible for obvious reasons, because we cannot delete a cell without deleting a row
# Overwriting
my_sqlite3_database.get_table("users").set_to_cell(key="1",
                                                   column_name="lastname",
                                                   new_value="Petrov")

# Receiving
print(my_sqlite3_database.get_table("users").get_from_cell(key="1",
                                                           column_name="lastname"))

# ====================================================Useful things====================================================

# In order to get all the unique identifiers from the table, you can call the 'get_all_keys` method.
# It will return a list with values.
print(my_sqlite3_database.get_table("users").get_all_keys())

# Some methods have a hidden `commit` argument, it is responsible for the immediate approval of data in the database.
# (Sometimes it happens that to increase the speed of the database, you can commit much less often than with each command)
my_sqlite3_database.get_table("users").commit()

# The first useful property of the Table class is `status'. It can be useful when you need to understand whether there
# is any data in balitsa or not.
print(my_sqlite3_database.get_table("users").status)

# The 'column_names` property contains the names of columns in the table (Although the name speaks for itself)
print(my_sqlite3_database.get_table("users").column_names)

# The `columns_count` property contains the number of columns in the table
print(my_sqlite3_database.get_table("users").columns_count)

# The `count` property contains the number of rows in the table
print(my_sqlite3_database.get_table("users").count)


# Conclusion



