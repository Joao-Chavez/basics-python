
### Functions en python ###

# Ejemplos de python functions

## EJEMPLO 1: suma de dos numeros 
def sumar(num1, num2):
    reaultado = num1 + num2
    return reaultado
print(sumar(3,5)) #Aquí llama la función para mostrarla

## EJEMPLO 2: función para imprimir un saludo
def saludo(nombre):
    print("Hola " + nombre + ", bienvenida")
saludo("Joao")

## EJEMPLO 3: calcular el área de un triángulo 
def area_de_rectangulo(base, altura):
    area = base * altura
    return area
print(area_de_rectangulo(4, 6))

#Ejemplos de default parameters

## EJEMPLO 1: función que suma dos números, 
    # pero si no se especifica el segundo número, se toma por defecto el valor 0
def suma(num1, num2 = 0):
    resultado = num1 + num2
    return resultado
print(suma(8, 5))
print(suma(3)) #El segundo parametro es 0 por defecto

##  EJEMPLO 2: función que imprime la bienvenida, 
    # pero si no se especifica el nombre, se toma por defecto "compa"
def saludar_parameter (nombre_parameter = "compa"):
    print("Hola " + nombre_parameter + ", bienvenido!")
saludar_parameter("Joao")
saludar_parameter() #El segundo parametro

## EJEMPLO 3: función que calcula el área de un rectángulo, 
    # pero si no se especifica la altura, se toma por defecto el valor 1
def area_rectangulo(base, altura = 1):
    area = base * altura
    return area 
print(area_rectangulo(5, 6))
print(area_rectangulo(4))

#Ejemplos de keyword arguments

##EJEMPLO 1: Imprime mensaje personalizado utilizando dos argumentos
def bienvenida(nombre, apellido, saludo="Hola"):
    mensaje = saludo + " " + nombre + " " + apellido
    print(mensaje)
bienvenida(nombre="Joao", apellido="Chávez")
bienvenida(nombre="Hugo", apellido="Calderón", saludo="Buenas")

##EJEMPLO 2: suma una lista de numeros y poder especificar si se quiere redondear
def suma_lista (numeros, redondear = False):
    suma = sum(numeros)
    if redondear:
        suma = round(suma)
    return suma
numeros = [1.5, 2.7, 3.3, 4.8]
print(suma_lista(numeros))
print(suma_lista(numeros, redondear=True))

##Ejemplo 3: Crea un diccionario y poder especificar si se quiere asignar un valor 
def add_diccionario(keys, value=None, default=False):
    diccionario = {}
    for key in keys: #Keys es para especificar la lista de claves
        if default: #default es para saber si se desea incluir el valor
            diccionario[key] = value #value es para especificar el valor
        else:
            diccionario[key] = None
    return diccionario
keys = ["a", "b", "c"]
print(add_diccionario(keys)) #imprime NONE
print(add_diccionario(keys, value=1, default=True)) #imprime 1