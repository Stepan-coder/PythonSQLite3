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
* `create_table` - This **method** creates a table in the database
* `get_table` - This **method** get the "Table" object for further interaction with it.

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

### Examples