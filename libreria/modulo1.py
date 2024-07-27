import sqlite3

class db:
    def __init__(self, ruta_db):
        self.ruta_db = ruta_db
        self.conexion = sqlite3.connect(ruta_db)
        self.cursor = self.conexion.cursor()

    def crear_tabla(self, nombre_tabla, columnas):
        """Crea una tabla en la base de datos especificada."""
        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({columnas})")
            self.conexion.commit()
            print(f"Tabla '{nombre_tabla}' creada exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def insertar_registro(self, nombre_tabla, columnas, valores):
        """Inserta un registro en una tabla específica de la base de datos."""
        try:
            self.cursor.execute(f"INSERT INTO {nombre_tabla} ({columnas}) VALUES ({', '.join(['?'] * len(valores))})", valores)
            self.conexion.commit()
            print("Registro insertado exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar el registro: {e}")

    def consultar_datos(self, nombre_tabla):
        """Consulta y muestra todos los datos de una tabla."""
        try:
            self.cursor.execute(f"SELECT * FROM {nombre_tabla}")
            filas = self.cursor.fetchall()
            for fila in filas:
                print(fila)
        except sqlite3.Error as e:
            print(f"Error al consultar los datos: {e}")

    def cerrar_conexion(self):
        """Cierra la conexión con la base de datos."""
        self.conexion.close()
        print("Conexión cerrada.")
