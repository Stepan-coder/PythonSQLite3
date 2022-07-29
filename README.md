# The simplest SQLile3 ORM for non - production develop :)

## Introduction

Due to the fact that I quite often visit various contests, competitions, hackathons and project shifts, I have an urgent need for my own module for working with the database. You will ask why? In fact, everything is very simple - when you have an extremely limited time frame, then you do not have time to develop and debug SQL queries. Yes, it's not efficient. Yes, it's not for production. `BUT!` With this module you can create and manage tables in a database very quickly, simply and easily. Record, modify, add, delete rows, cells, tables.  
Another useful app is [SQLiteStudio](https://sqlitestudio.pl). With this application under `windows` you can visually view and edit SQLite3 database.

## Project structure

To run the module, you need to move the [SQLite3Module](SQLite3Module) folder to the `root` of your project. Project structure required to launch:  

|-> `Your project folder`  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `SQLite3Module`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `__init__.py`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `SQLite3_base.py`   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `SQLite3_table.py`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `SQLite3_DBType.py`  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `__main__.py`  

* `__init__.py` - The file in which all the files necessary for the operation of the module are initialized 
* `SQLite3_base.py` - This file implements a class for creating and managing a database 
* `SQLite3_table.py` - This file implements the table class in the database
* `SQLite3_DBType.py` - This file implements [Enum](https://docs.python.org/3/library/enum.html) of possible data types

## Documentation

#### SQLite3_DBType.py

There are several generally accepted data types for storing information in the database, but due to the brevity of the `SQLite3`, only some are used:

* `NULL` - Just nothing, nothing at all.  
* `INTEGER` - An integer such as 1, 2, 10, 100000, -1000000000.  
* `REAL` - Floating point number, e.g. 1.5.  
* `TEXT` - Plain text like in sms.  
* `BLOB` - Binary representation of large objects stored exactly as it was entered. Simply put 101.  

#### SQLite3_base.py

* `cursor` - This **property** returns the cursor for the database (directly the thing that works with database cells)  
* `connector` - This **property** returns the connector for the database (the thing through which the connection to the database is established)  
* `tables` - This **property** returns the list of table names
* `add_table` - This **method** creates a table in the database
* `get_table` - This **method** get the "Table" object for further interaction with it.
* `delete_table` - This **method** delete table with `table_name` name

#### SQLite3_table.py

* `__nonzero__` - This **method** returns a `bool` whether the table is declared.
* `column_names` - This **property** returns a list of column names.
* `create_table` - This **method** creates a table with the specified columns. If `primary_key` is not specified, then the first column will be considered the identifier, otherwise - the one selected by the user.  
* `get_from_cell` - This **method** returns the value from the cell located in the column `column_name` and the row with the identifier `key`.
* `set_to_cell` - This **method** writes the value of new_value in the column_name column to the string with the id `key`.
* `add_row` - This **method** adds a new row to the table
* `get_row` - This **method** gets values from all columns of the `row` table
* `delete_row` - This **method** removes the `row` from the table
* `get_column` - This **method** returns all values from the `column_name` column
* `get_all_keys` - This **method** returns all values of all identifiers (a column whose values are unique for each row)
* `commit` - This **method** confirms the entry in the table


## Examples

### DataBase

To work with `SQLite3Module`, it is enough to simply import it into your project, the main file is `SQLite3Module/SQLite3_base.py `.  
```Python3
import os
from SQLite3Module.SQLite3_base import *


my_sqlite3_database = DataBase(path=os.getcwd(), filename="my_BD.sqlite3")
```
Now you don't need to know the `SQL` language to create a table, just call the appropriate method and pass the appropriate parameters to it. 
*In this concrete case, the unique key `primary_key` will be the column `user_id'.*
```Python3
my_sqlite3_database.add_table(tablename="users",
                              columns={"user_id": DBType.INTEGER,
                                       "firstname": DBType.TEXT,
                                       "lastname": DBType.TEXT,
                                       "score": DBType.REAL})
```
Yes, we can creating one more table :)
To change the `primary_key`, when initializing the table, you need to explicitly specify the column that you want to make the main one.
For example, like this:
```Python3
my_sqlite3_database.add_table(tablename="products",
                              columns={"product_id": DBType.INTEGER,
                                       "name": DBType.TEXT,
                                       "description": DBType.TEXT},
                              primary_key="product_id")
```
Naturally, what can be created can be deleted.  
**Deleting a table is not a cancellable action!!!**
```Python3
my_sqlite3_database.delete_table(table_name="users")
```
To see which tables the database consists of and in what state they are now, you can run the following code.
```Python3
print(my_sqlite3_database.get_table("users"))
```
In the terminal you will see the following
```
+-------------------------------------------------------------+
|                           DataBase                          |
+----------+------------+---------------+------------+--------+
|   Name   |    Type    | Columns count | Rows count | Status |
+----------+------------+---------------+------------+--------+
| products | <DataBase> |       3       |     0      |  EMPTY |
|  deals   | <DataBase> |       3       |     0      |  EMPTY |
+----------+------------+---------------+------------+--------+
```

### Table

So, the database is ready, only the table with users should be returned back (otherwise it doesn't work out well))  
*I'll just recreate the database and comment on deleting the "users" table*
To add a new entry to the table, you need to do 2 things, understand what and to which table we add)))

The "add_row" method accepts a dictionary, where the key is the column name, and the value is the value
that needs to be written to this column.
```Python3
my_sqlite3_database.get_table("users").add_row(row={"user_id": 1,
                                                    "firstname": "Ivan",
                                                    "lastname": "Ivanov",
                                                    "score": 3.14159})
```
Now we can try to get this string from the database and see what will be returned to us. The `key` parameter corresponds to a string with such a unique identifier as `key` (`primary_key`, which we specified earlier)
```Python3
print(my_sqlite3_database.get_table("users").get_row(key="1"))
```
In the terminal you will see the following
```
{'user_id': 1, 'firstname': 'Ivan', 'lastname': 'Ivanov', 'score': 3.14159}
```
Similarly to records, we can delete the row we need from the table as follows:
```Python3
my_sqlite3_database.get_table("users").delete_row(key="1")
```
With individual cells, you can do all the same actions: overwriting and receiving. Looking)
*Deletion is not possible for obvious reasons, because we cannot delete a cell without deleting a row*

#### Overwriting
```Python3
my_sqlite3_database.get_table("users").set_to_cell(key="1",
                                                   column_name="lastname",
                                                   new_value="Petrov")
```
#### Receiving
```Python3
print(my_sqlite3_database.get_table("users").get_from_cell(key="1",
                                                           column_name="lastname"))
```

## Useful things
In order to get all the unique identifiers from the table, you can call the 'get_all_keys` method. It will return a list with values.
```Python3
print(my_sqlite3_database.get_table("users").get_all_keys())
```
Some methods have a hidden `commit` argument, it is responsible for the immediate approval of data in the database. (Sometimes it happens that to increase the speed of the database, you can commit much less often than with **each command**)
```Python3
my_sqlite3_database.get_table("users").commit()
```

