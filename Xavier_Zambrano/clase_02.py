## Cadenas de Variables

name = 'Xavier'
last_name = 'zambrano'

print (name + '' + last_name)

print (10 * name)

#para una limpieza de datos quitar tildes o colocar en mayusculas y minusculas
print (len(name) )  #conteo de palabra
print(name. lower())  #Minusculas
print (name.upper())    #Mayusculas
print (name.strip('X')) #Elimina espacios en blanco adicionales y caracteres especificos del inicio o final
print (name.strip('r')) #Elimina espacios en blanco adicionales y caracteres especificos del inicio o final


## espacio de memoria  (listas)

a = [1,2,3,4,5]  #arreglo
b=a
print(a)
print (b)
del a[0]  #elimina el espacio de la memoria selecionada
print(a)
print (id(a)) #saca el espacio de memeoria asiganado
print(id(b)) #saca el espacio de memeoria asiganado

c = a[:] # es una forma de arreglo mas acortada
print (c)
print(id(c))

a.append(7) # se agrega un valor especifico al ultimo punto
print(a)