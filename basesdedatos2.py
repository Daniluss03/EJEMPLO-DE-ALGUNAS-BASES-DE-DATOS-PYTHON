# EJEMPLO-DE-ALGUNAS-BASES-DE-DATOS-PYTHON
mport sqlite3
conexion=sqlite3.connect("usuarios_autoincremental.db")
cursor=conexion.cursor()

#cursor.execute('''
 #    CREATE TABLE usuarios(
  #       dni VARCHAR(9) PRIMARY KEY,
    #     nombre VARCHAR(100),
   #      edad INTEGER,
    #     emil VARCHAR(100) 
 #    )
  #   ''')
#usuarios=[
 #   ('11231241a','Mario',51,'mario@gmail.com'),
  #  ('22222241B','Mercedez',70,'merceditas@gmail.com'),
   # ('3333331C','canario',61,'canario123@gmail.com'),                            #Estas son tuplas
    #('44444441D','danilo',20,'danilusmaximudecimusmeridius@gmail.com'),
    # ('555555E','jorge',20,'jorge@gmail.com'),
#]   
# 
# 
#   identificador utomatico 
#cursor.executemany("INSERT INTO  usuarios  VALUES (?,?,?,?)",usuarios)
#cursor.execute('''
 #     CREATE TABLE productos ( 
  #      id INTEGER PRIMARY KEY AUTOINCREMENT,
   #     nombre VARCHAR(100) NOT NULL,
     #   marca VARCHAR (50)NOT NULL,
    #    precio FLOAT NOT NULL
 #     )
#''')


#productos=[
 #   ('Teclado','sony',19.95),
  #  ('pantalla 19','LG',89.95)
#]
#cursor.executemany("INSERT INTO  productos  VALUES (null,?,?,?)",productos)


#buscar los productos desde la base y mostrarlos

#cursor.execute("SELECT* FROM productos")
#productos = cursor.fetchall()
#for productos in productos:
   # print(productos)



cursor.execute('''
       CREATE TABLE usuarios (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          dni VARCHAR(9)UNIQUE,
          nombre VARCHAR(100),
          edad INTEGER,
          email VARCHAR (100)
         )
      ''')
usuarios = [
    ('11231241a','Mario',51,'mario@gmail.com'),
    ('22222241B','Mercedez',70,'merceditas@gmail.com'),
    ('3333331C','canario',61,'canario123@gmail.com'),                           
    ('44444441D','danilo',20,'danilusmaximudecimusmeridius@gmail.com'),
    ('555555E','jorge',20,'jorge@gmail.com'),
 ]

cursor.executemany("INSERT INTO  usuarios  VALUES (null,?,?,?,?)",usuarios)

conexion.commit()
conexion.close() 
