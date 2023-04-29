
### CONTROL FLOW EN PYTHON ###

# Ejercicios de if...else statements

def example1_if_else():
    numero = -3
    if numero >= 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")

def example2_if_else():
    usuario_autenticado = True
    if usuario_autenticado:
        print("Acceso permitido")
    else:
        print("Acceso no permitido")

def example3_if_else():
    numero = 9
    if numero % 2 == 0:
        print("Numero par")
    else:
        print("Numero impar")

example1_if_else()
example2_if_else()
example3_if_else()

# Ejercicios de ternary operators

def example1_ternary_operator():
    edad = 22
    es_mayor_de_edad = True if edad > 18 else False
    print("¿Es mayor de edad?", es_mayor_de_edad)

def example2_ternary_operator():
    numero = -8
    valor_absoluto = numero if numero >= 0 else -numero
    print("El valor absoluto de", numero, "es", valor_absoluto)

def example3_ternary_operator():
    administrador = True
    mensaje = "Bienvenido" if administrador else "No eres administrador"
    print(mensaje)

example1_ternary_operator()
example2_ternary_operator()
example3_ternary_operator()

# Ejercicios de for loop with range 

def example1_for_loop():
    for i in range(5):
        print(i)

def example2_for_loop():
    suma = 0
    for i in range(1,11):
        suma += i
        print("La suma es:", suma)

def example3_for_loop():
    for i in range(0, 9, 2):
        print(i)

example1_for_loop()
example2_for_loop()
example3_for_loop()

# Ejercicios de while

def example1_while():
    i = 0
    while i < 6:
        print (i)
        i += 1

def example2_while():
    suma = 0
    i = 1
    while i <= 10:
        suma += i
        i += 1
        print("La suma es:", suma)

def example3_while():
    numero = 0
    while numero < 5:
        numero = int(input("Ingresa un número mayor o igual a 5: "))
        print("El numero ingresado es:", numero)

example1_while()
example2_while()
example3_while()