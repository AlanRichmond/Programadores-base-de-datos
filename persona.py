from datetime import datetime

class Persona:
    def __init__(self, nombre, apellido, dni, fechaDeNacimiento, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.__dni = dni
        self.__fechaDeNacimiento = fechaDeNacimiento
        self.nacionalidad = nacionalidad
            
    def __str__(self):
        return (f" la persona se llama {self.nombre} {self.apellido}")
    
    def get_dni(self):
        return (f"el dni de la persona es {self.__dni}")
    
    def get_fechaNacimiento(self):
        return (f"el dni de la persona es {self.__fechaDeNacimiento}")
    
    def edad(self):           
        # Obtener la fecha y hora actual
        fecha_actual = datetime.now()

        # Extraer el día, mes y año
        dia_actual = int(fecha_actual.day)
        mes_actual = int(fecha_actual.month)
        ano_actual = int(fecha_actual.year)

        partes = self.__fechaDeNacimiento.split('/')
        year = partes[-1]
        mes = partes[1]
        dia = partes[0]
        year_entero = int(year)
        mes_entero = int(mes)
        dia_entero = int(dia)
        
        edad_actual = ano_actual - year_entero
        
        if(mes_actual >= mes_entero):
            if(dia_actual >= dia_entero):
                return edad_actual
            elif(dia_actual < dia_entero):
                return edad_actual -1
        
        return edad_actual - 1    
      
        
        






