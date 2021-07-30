import sqlite3

conexion=sqlite3.connect("ejemplo.db")

#crar un cursor
cursor=conexion.cursor()
#esto se conoce como consulta
#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER,email VARCHAR(100))")


#insertar un regitro
#cursor.execute("INSERT INTO usuarios VALUES('Hector',27,'danilo@gmail.com')")


#recuperar el primer registro

#cursor.execute("SELECT * FROM  usuarios")
#print(cursor)

#recuperar el primer registro en forma de tupla  con el metodo fetchone
#usuario=cursor.fetchone()
#print(usuario)
"""usuarios=[
    ('Mario',51,'mario@gmail.com'),
    ('Mercedez',70,'merceditas@gmail.com'),
    ('canario',61,'canario123@gmail.com'),                            #Estas son tuplas
    ('danilo',20,'danilusmaximudecimusmeridius@gmail.com'),
]"""
#ejecutar varios 
#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)",usuarios)
cursor.execute("SELECT * from  usuarios")
usuarios=cursor.fetchall()

for usuario in usuarios:
    print(usuario)

#confirmar cambios de  bases de datos
conexion.commit()
conexion.close()
