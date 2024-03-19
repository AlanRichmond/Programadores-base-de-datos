import sqlite3
from tabulate import tabulate

# Conector a la base de datos
def conexion():
    conexion = sqlite3.connect("programadores.db")
    return conexion

# Crear un cursor para ejecutar comandos SQL
def crearCursor(conec):
    cursor = conec.cursor()
    return cursor

# Crea la tabla si no existe 
def crearTabla():
    cursor = conexion()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS programadores (
            id_programador INTEGER PRIMARY KEY,
            nombre TEXT,
            apellido TEXT,
            edad INTEGER,
            lenguaje TEXT,
            anios_experiencia INTEGER
        )
    ''')
    
#recibe los atributos de la clase programador
#inserte los atributos en sus respectivas posiciones de la tabla en la base de datos
def insertar(programador):
    conec = conexion()
    cursor = crearCursor(conec)
    crearTabla()
    cursor.execute("INSERT INTO programadores (nombre, apellido, edad, lenguaje, anios_experiencia) VALUES (?, ?, ? , ?, ?)",
               (programador.nombre, programador.apellido, programador.edad(), programador.lenguajeDeProgramacion,programador.aniosProgramando))
    cerrarConexion(conec)
 
 
#recibe el nombre a cambiar y el id del programador a cambiar
#cambia el nombre del id programador recibido 
def editarNombre(nombreNuevo, id):
    conec = conexion()
    cursor = crearCursor(conec)   
    cursor.execute(f"UPDATE programadores SET nombre = '{nombreNuevo}' WHERE id_programador = {id}")
    cerrarConexion(conec)
    
    
#recibe el nombre del programador que se quiere eliminar
def eliminarNombre(programadorEliminar):
    conec = conexion()
    cursor = crearCursor(conec)   
    cursor.execute(f"DELETE FROM programadores WHERE nombre = '{programadorEliminar}' ")
    cerrarConexion(conec) 


# muestra por la terminal la tabla 
def mostrarTabla():
    conec = conexion()
    cursor = crearCursor(conec)
    cursor.execute("SELECT * FROM programadores")
    registros = cursor.fetchall()
    
    tabla = []
    for registro in registros:
        tabla.append(registro)
    print("\n\n\n\n\n\n")
    print(tabulate(tabla, headers=['id', 'Nombre', 'Apellido', 'Edad', 'Lenguajes','Experiencia']))
    cerrarConexion(conec)
    
    
# recibe un atributo de la base de datos para mostrar por pantalla la tabla ordenada desde ese atributo,
# de manera Descendente
def mostrarTablaDescPor(atributo):
    conec = conexion()
    cursor = crearCursor(conec)
    cursor.execute(f"SELECT * FROM programadores ORDER BY {atributo} DESC")
    registros = cursor.fetchall()
    tabla = []
    for registro in registros:
        tabla.append(registro)
    print("\n\n\n\n\n\n")
    print(tabulate(tabla, headers=['id', 'Nombre', 'Apellido', 'Edad', 'Lenguajes','Experiencia']))
    cerrarConexion(conec)


# recibe un atributo de la base de datos para mostrar por pantalla la tabla ordenada desde ese atributo,
# de manera Ascendente
def mostrarTablaAscPor(atributo):
    conec = conexion()
    cursor = crearCursor(conec)
    cursor.execute(f"SELECT * FROM programadores ORDER BY {atributo} ASC")
    registros = cursor.fetchall()
    tabla = []
    for registro in registros:
        tabla.append(registro)
    print("\n\n\n\n\n\n")
    print(tabulate(tabla, headers=['id', 'Nombre', 'Apellido', 'Edad', 'Lenguajes','Experiencia']))
    cerrarConexion(conec)
    
    
# Guardar (commit) los cambios en la base de datos
# Cierra la conexión
def cerrarConexion(conec):   
    conec.commit()
    conec.close()