## Ejercicio 1
​
# Crear una funcion que reciba un numero como argumento y devuelva el largo de este numero
# ​
# **Ejemplo**
# 
# `number_length(10) -> 2`
# ​
# `number_length(10000) -> 5`
# ​
# `number_length(4321) -> 4`
# ​
# **Restricciones**
# - El numero no puede ser negativo
# - El numero que se MANDA a la funcion tiene que ser de tipo INT
# - **NO** se puede utilizar el metodo length

### Solución del ejercicio

def len_number(number):
    if type(number) != int:
        return 'Ingresa un número por favor'
    elif number < 0 :
        return 'Ingresa números positivos por favor'
    count = 0
    number_to_string = str(number)
    for character in number_to_string:
        count += 1
    return count

len_number(5555555)
len_number('56')
len_number(-5)
len_number(True)
