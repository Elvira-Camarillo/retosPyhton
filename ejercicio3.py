## Ejercicio 3
# Crear una funcion que devuelva el factorial de un numero
# **Ejemplos**
# `factorial(3) -> 6` (3*2*1)
# `factorial(4) -> 24` (4*3*2*1)
# **Tips**
# - Investigar que demonios es recursividad

def factorial(number):
    is_number = isinstance(number,int)
    if is_number != True:
        return 'Ingresa un número por favor'
    if number > 1:
        return number * factorial(number -1)
    else:
        return 1

factorial(5)
factorial('2')


# Form 2
from math import factorial
factorial(5)