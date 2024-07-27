from libreria.modulo1 import db

mi_db = db('Testing.db')

# Uso de la clase db
#mi_db.consultar_datos_tabla('jugadores')
mi_db.filtrar_datos_tabla("jugadores", "creditos", "> 10")
mi_db.cerrar_conexion()