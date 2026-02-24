#Practica 4-Funcion Calculadora

print("---------Mi calculadora -----------")
num_1 = int(input("Escribe el primer valor : "))
num_2 = int(input("Escribe el segundo valor: "))
ope= input("¿Cual operacion deseas hacer? +, -, *, / -> ")
def suma(num_1, num_2):
    return num_1 + num_2

if ope == "+" :
    resultado = suma(num_1, num_2)
    print("El resultado de la suma es: ", resultado)

def resta(num_1, num_2):
    return num_1 - num_2

if ope == "-":
    resultado = resta(num_1, num_2) 
    print("El resultado de la resta es:", resultado)

def multi(num_1, num_2):
    return num_1 * num_2

if ope == "*":
    resultado = multi(num_1, num_2) 
    print("El resultado de la multi es:", resultado)

def divi(num_1, num_2):
    return num_1 / num_2

if ope == "/":
     resultado = divi(num_1, num_2) 
     print("El resultado de la division es:", resultado)
  

  


