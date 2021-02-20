#Crear una función que reciba un número como argumento y devuelva el largo de este número

def len_number(number):
    count = 0
    if isinstance(number,int):
        if number < 0:
            print('Ingresa un número positivo por favor')
        else:
            number_to_string = str(number)
            for caracter in number_to_string:
                count += 1
            print(count)
    else:
        print('Ingresa un número por favor')

len_number(5555555)
len_number('56')
len_number(-5)
            
