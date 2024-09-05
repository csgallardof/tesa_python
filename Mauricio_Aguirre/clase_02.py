## cadena de variables

Name="Mauricio"
last_name="Aguirre"

print(Name + ' ' + last_name)

print (10 * Name)

print(len(Name))
print(Name.lower) ##CARACTERES EN MAYUSCULAS
print(Name.upper) ## caracteres en minusculas

print(last_name.strip())


## espacio de memorio 

a = [1,2,3,4,5]
b=a
print(a)
print(b)
del a[0]
print(a)
print(id(a))
print(id(b))

c=a[:]
print(c)

a.append(7)

print(a)