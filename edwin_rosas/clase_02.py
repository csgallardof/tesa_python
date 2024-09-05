## cadenas de variables

name = 'Edwin Leonardo'
lastname = 'Rosas Yague'
name2 = '  Edwin Leonardo   '

print (name + ' ' + lastname)

## multiplicacion de string
print (10 * name )

##obtener el tamaño de la cadena de caracteres

print(len(name))

##caracteres todo en minuscula
print(name.lower())

##caracteres todo en mayuscula
print(name.upper())

##strip elimina espacios en blanco al inicio o final de la cadena
print('Original' + ' ' + name2)
print('sin caracteres en blanco inicio/fin' + ' ' +name2.strip())
