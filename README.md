# pandas-ex-2
This project contains some examples of SQL alchemy and pandas to perform Extract, Transform, and Load (ETL) jobs.
The end goal is to re-use the maximum amount of ETL code possible. There are already many extensions in both
the sqlalchemy and pandas modules that can:

## [pandas](https://pandas.pydata.org/)
* read and write multiple data types including csv, Excel, cloud providers
* identify data types, convert values and clean data from real input
* allow for robust replacement and filtering logic that embrance Python language features

## [sqlalchemy](https://www.sqlalchemy.org/)
* handles queries to MS SQL Server, MySQL, Postgres, and SQLite databases
  - also has an in-memory provider thorugh SQLite engine
* full ORM to dynamically produce DDL and DML statements through class design and registry
* always capable of dropping to a native SQL statement or batch ingrained within the core toolkit

Both modules have active communities and cookbooks of common use cases available.
