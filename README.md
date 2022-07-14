# The simplest SQL connector for non - production develop :)

## Introduction

Due to the fact that I quite often visit various contests, competitions, hackathons and project shifts, I have an urgent need for my own module for working with the database. You will ask why? In fact, everything is very simple - when you have an extremely limited time frame, then you do not have time to develop and debug SQL queries. Yes, it's not efficient. Yes, it's not for production. `BUT!` With this module you can create and manage tables in a database very quickly, simply and easily. Record, modify, add, delete rows, cells, tables.

Another useful app is [SQLiteStudio](https://sqlitestudio.pl). With this application under `windows` you can visually view and edit SQLite3 database.


## Project structure

To run the module, you need to move the `SQLite3Module` folder to the `root` of your project. Project structure required to launch:

`Your project folder`  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `SQLite3Module` 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `__init__.py`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `SQLite3_base.py`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `SQLite3_table.py`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `SQLite3_DBType.py`  
|-> `__main__.py`  