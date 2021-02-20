### Ejercicio 2
#
# Crear una función que reciba dos números como argumentos (número,longitud), y devolver una lista con los múltiplos del número dada la longitud.
# list_of_multiples(7,5) -> [7,14,21,28,35]
# **Restricciones**
# - El numero no puede ser negativo
# - El numero que se MANDA a la funcion tiene que ser de tipo INT

def list_of_multiples(number,len_multiples):
    if type(number) != int or type(len_multiples) != int:
        return 'Ingresa un número por favor'
    elif number < 0 or len_multiples <0 :
        return 'Ingresa números positivos por favor'
    multiples_number = []
    for count in range(1,len_multiples+1):
        multiple = number * count
        multiples_number.append(multiple)
    return multiples_number
        
list_of_multiples(2,6)

