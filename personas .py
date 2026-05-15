# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Crear 2 objetos
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)

# Imprimir los datos desde fuera de la clase
print("Datos de la Persona 1")
print("Nombre:", persona1.nombre,
      )
print("Edad:", persona1.edad)

print("\nDatos de la Persona 2")
print("Nombre:", persona2.nombre)
print("Edad:", persona2.edad)