print("Programacion POO")
# Definicion de clases
class Perro:
    # funciones dentro de la clas
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self,nombre,edad):
            print(f"Nombre : {nombre} edad : {edad}")


# zona de creacion de objeto
pitbull=Perro()

# zona de uso de objetos
pitbull.Datos_perro("body",4)
pitbull.morder()
