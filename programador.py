from persona import Persona


class Programador(Persona):
    def __init__(self, nombre, apellido, dni, fechaDeNacimiento, nacionalidad,
                lenguajeDeProgramacion, trabajo, aniosProgramando):
        super().__init__(nombre, apellido, dni, fechaDeNacimiento, nacionalidad)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion
        self.trabajo = trabajo
        self.aniosProgramando = aniosProgramando 
        
    def __str__(self):
        return (f"el programador maneja {self.lenguajeDeProgramacion}")
    
    def nivelDeProgramador(self):
        if(self.aniosProgramando > 10):
            return(f"{self.nombre} es un programador Senior")
        elif(self.aniosProgramando >= 2 & self.aniosProgramando <10):
            return(f"{self.nombre} es un programador Semi-Senior")
        else:
            return(f"{self.nombre} es un programador Junior")
