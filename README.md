# Bono-DB-Manager 🛢                                                                                                                          

Bono-DB is a Python library designed to simplify SQLite database management. It provides an intuitive interface for creating, manipulating and interacting with databases, allowing developers to focus on application logic rather than technical database details.
This project can be your first good first issue.

## Badge
Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## Contributing

Contributions are always welcome!

See `contributing.md` to see how to get started.


## Usage/Examples

```Python
from library.DataBase import DB

# Create an instance of the DB class
my_db = DB('my_database.db')

# Use the DB class
my_db.create_table('players', 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, score INTEGER NOT NULL, credits INTEGER NOT NULL')
my_db.insert_record('players', 'name, score, credits', ('John', 100, 50))
my_db.query_table_data('players')
my_db.filter_table_data('players','credits','>10')
my_db.close_connection()

```


## Author

- [@AbelolDev](https://github.com/AbelolDev)

