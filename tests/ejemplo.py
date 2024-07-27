from libreria.modulo1 import *

mi_db = db('Testing.db')

# Uso de la clase db
mi_db = db('mi_base_de_datos.db')
mi_db.crear_tabla('jugadores', 'id INTEGER PRIMARY KEY, nombre TEXT, puntaje INTEGER, creditos INTEGER')
mi_db.insertar_registro('jugadores', 'nombre, puntaje, creditos', ('Juan', 100, 50))
mi_db.consultar_datos('jugadores')
mi_db.cerrar_conexion()