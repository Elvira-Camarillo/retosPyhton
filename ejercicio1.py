# Crear una función que reciba un número como argumento y devuelva el largo de este número

# Ejercicio 1

def len_number(number):
    if type(number) != int:
        return 'Ingresa un número por favor'
    elif number < 0 :
        return 'Ingresa números positivos por favor'
    else:
        count = 0
        number_to_string = str(number)
        for caracter in number_to_string:
            count += 1
        return count

len_number(5555555)
len_number('56')
len_number(-5)