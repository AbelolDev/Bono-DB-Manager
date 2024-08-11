from library.DataBase import DB

# Create an instance of the DB class
my_db = DB('my_database.db')

# Use the DB class
my_db.create_table('players', 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, score INTEGER NOT NULL, credits INTEGER NOT NULL')
my_db.insert_record('players', 'name, score, credits', ('John', 100, 50))
my_db.query_table_data('players')
my_db.filter_table_data('players','credits','>10')
my_db.cipher('players','password')
my_db.close_connection()
