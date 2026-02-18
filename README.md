# Práctica 1 - Flujo Básico de git y github
Es el metodo de modificacion que nos enseño el profesor sobre el cambio

# Practica 2 - Conceptos Báscos de Base De Datos
Documentar en el archivo README.md del repositorio flujoBasico contestando las siguientes preguntas:

1._¿Qué es una Base De Datos Relacional?
una base de datos relacional es donde se puedene guardar los datos o mejor dicho organizar los datos importantes que seria como la informacion

2._¿Qué es una Tabla en el contexto Base De Datos Relacionales?es un tipo de estructura que almacena los tipos de datos y los organiza de manera en columnas y/o filas

3._¿Qué es una relación en el contexto de Base De Datos Relacionales?es un tipo de vinculo de tipos de elementos 

4._¿Qué representa una columna en el contexto de Base De Datos Relacionales? una manera de describir el tipo de almacenamiento de los registros de ususarios que serian su informacion

5._¿Qué representa un renglón en el contexto de Base De Datos Relacionales? es un tipo de registo en una fila

6._¿Qué es un motor de base de datos relacional?
es una manera de crear o mejor dicho administras los datos

7._¿Cuáles son los motores de bases de datos relacionales mas populares?los motores de bases de datos son :MQSL,SQLite, Oracle Database y muchos mas.

8._¿Cuál es el motor de base datos ligero que no necesita un servidor? el motor ligero seria el SQLite ya que no necesita un servicio de base de datos.

9._¿Qué significa SQL en el contexto de base datos relacionales?significa que es lenguaje de consulta estructurado

10._¿Cuáles son los elementos de un sistema de información basado en base de datos relacionales? el motor de base de datos, las columnas, el lenguaje SQLite, el base de datos e interfaces de usuario


## investigacion 

## clases vs objetos


 class celular:
     def __init__(self, marca, modelo, bateria):
         self.marca = marca
         self.bateria = bateria 
         self.modelo = modelo
     def Llamar(self):
      print("Sonando")

      def cargador(self):
       self.bateria = 100

       def apagar(self):
       print("Apagado")

mi_tel = celular("Samsung", "galaxy09", 70)


## Metodo


 class Usuario:
     def __init__(self, nombre):
        self.nombre = nombre

u = Usuario("Carlos")
print(u.nombre)

## Parametro self


 class Cuenta: 
   def __init__(self, usuario):
   self.dueño = usuario

def mostrar(self):
 print("Cuenta de", self.usuario)


## encapsulamiento

  class Cajas:
    def __init__(self):
         self.__clave = 1235

     def verifica(self, c)
      return c == self.clave 


## Herencia
 "Super clase"
 class Transporte:
   def manejar(self):
      print("Manejando")
 "subclase"
class bicicleta:
    pass

class bocho:
    pass

## Composicion

 class teclado:
  def escribir(self):
   print("Escribir")

class laptop:
 def __init__(self):
 self.teclado = teclado()

## Estado 
 class cuentaBVV:
  def __init__(self)
   self.sald = 0


def deposito(self, mone):
 self.sald += mone
