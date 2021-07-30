# EJEMPLO-DE-ALGUNAS-BASES-DE-DATOS-PYTHON
import sqlite3

conexion= sqlite3.connect("usuarios_autoincremental.db")
cursor=conexion.cursor()

#realizar consultas
#cursor.execute("SELECT * FROM usuarios WHERE edad=20")
#usuario = cursor.fetchall()

# renombrar campos de un usuario    ojo con el where  sino se actualiza todos los registros 
#cursor.execute("UPDATE usuarios SET nombre ='daniluss', WHERE  dni ='3333331C'")

#BORRAR UN USUARIO 
cursor.execute("DELETE  FROM  usuarios WHERE  dni ='3333331C'")

conexion.commit()
conexion.close()
