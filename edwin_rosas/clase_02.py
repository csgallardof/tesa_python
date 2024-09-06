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


##manejo de espacios de memoria

a = [1,2,3,4,5]
b= a
print (a)
print (b)
del a[0]
print (a)
print (a[2])
print (id (a))
print (id (b))
##le da el valor de la variable a a c pero en otro espacio de memoria
c=a[:]
print (c)

a.append(7)
print (a)
b.append(9)
print (b)
print (a)
print (id (c))
print (c)


