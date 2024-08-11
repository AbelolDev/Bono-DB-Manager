import sqlite3
import hashlib

class DB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        """Creates a table in the specified database."""
        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
            self.connection.commit()
            print(f"Table '{table_name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_record(self, table_name, columns, values):
        """Inserts a record into a specific table in the database."""
        try:
            self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(['?'] * len(values))})", values)
            self.connection.commit()
            print("Record inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting record: {e}")

    def query_table_data(self, table_name):
        """Queries and displays all data from a table."""
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"Error querying data: {e}")

    def filter_table_data(self, table, column, condition):
        """Searches for specific information in a column based on the set condition."""
        try:
            query = f"SELECT * FROM {table} WHERE {column} {condition}"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"Error querying data: {e}")

    def cipher(self, table, column):
        """Encrypts text in a column with SHA-256 protocol."""
        try:
            query = f"SELECT id, {column} FROM {table}"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            for row in rows:
                record_id = row[0]
                original_value = str(row[1])
                encrypted_value = hashlib.sha256(original_value.encode()).hexdigest()

                update_query = f"UPDATE {table} SET {column} = ? WHERE id = ?"
                self.cursor.execute(update_query, (encrypted_value, record_id))

            self.connection.commit()
            print("Encryption complete.")

        except sqlite3.Error as e:
            print(f"Error querying data: {e}")


    def close_connection(self):
        """Closes the connection to the database."""
        self.connection.close()
        print("Connection closed.")
