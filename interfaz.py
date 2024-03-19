from programador import Programador
import base_de_datos
import os


# pregunta por pantalla al usuario todos los atributos de la clase Porgramador 
# inserta los valores a la base de datos 
def preguntasProgramador():
    os.system("clear")
    print("Hola!\nSe le hara algunas preguntas para poder registrarlo en la base de datosz.\n")
    nombre = input("Cual es tu nombre? ")
    apellido = input("Cual es tu apellido? ")
    dni = int(input("cual es tu dni? "))
    fecha_nacimiento = input("cual es tu fecha de nacimiento?(formato XX/XX/XXXX) ")
    nacionalidad = input("Nacionalidad? ")
    lenguajePorgramacion = input("que lenguajes de programacion manejas? ")
    trabajo = input("tienes trabajo de programador (si/no)? ").lower()
    if(trabajo == "si"):
        experiencia = int(input("cuantos años tienes trabajando? "))
    else:
        experiencia = 0
    programador1 = Programador(nombre,apellido,dni,fecha_nacimiento,nacionalidad,lenguajePorgramacion,
            trabajo,experiencia)
    base_de_datos.insertar(programador1)


def mostrarTabla():
    print("TABLA: ")
    base_de_datos.mostrarTabla()
    
continuar = True
while(continuar == True):
    os.system("clear")
    consulta = int(input("""
                        OPCIONES
                     ------------------
                     1 - INSERTAR
                     2 - ELIMINAR (por nombre)
                     3 - EDITAR NOMBRE 
                     4 - MOSTRAR TABLA DE PROGRAMADORES
                     5 - MOSTRAR TABLA DE PROGRAMADORES POR MENOR..
                     6 - MOSTRAR TABLA DE PROGRAMADORES POR MAYOR..
                     7 - SALIR 
                     
                     ingrese numero: """))
    os.system("clear")
    
    if(consulta == 1):
        preguntasProgramador()
        os.system("clear")
        print("EL PROGRAMADOR SE INGRESO CORRECTAMENTE \n\n")

    elif(consulta == 2):
        mostrarTabla()
        nombreEliminar = input("\nCual es el nombre que quieres eliminar? ")     
        os.system("clear")
        base_de_datos.eliminarNombre(nombreEliminar)
        
    elif(consulta == 3):
        mostrarTabla()
        id_programador = int(input("\nCual es el id del programador que quieres cambiar? "))
        nombrecambiar = input("\nCual es el nuevo nombre? ")
        os.system("clear")
        base_de_datos.editarNombre(nombrecambiar,id_programador)
        
    elif(consulta == 4):
        mostrarTabla()
        
    elif(consulta == 5):    
        atributo = input("""
                         - Ingrese por que atributo quiere ordenar de manera Ascendente:
                         - (nombre | apellido | edad | lenguaje | anios_experiencia) 
                         - respuesta: """)
        os.system("clear")
        print("TABLA: ")
        base_de_datos.mostrarTablaAscPor(atributo)
    
    elif(consulta == 6):
        atributo = input(""" 
                         - Ingrese por que atributo quiere ordenar de manera Descendente:
                         - (nombre | apellido | edad | lenguaje | anios_experiencia) 
                         - respuesta: """)
        os.system("clear")
        print("TABLA: ")
        base_de_datos.mostrarTablaDescPor(atributo)
    
    elif(consulta == 7):
        print("Salio exitosamente.")
        continuar = False
        
    else:
        os.system("clear")
        print("no es un valor valido\n")
        
        
        
    if(continuar == True):
        seguirPreguntando = input("Quieres hacer otra instruccion? (si/no) ").lower()
        if(seguirPreguntando == "no"):
            continuar = False
        
    
    


