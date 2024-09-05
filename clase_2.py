## Cadenas de variables
name = 'Juan Moreno'
last_name = 'Moreno'

print(name + ' ' + last_name)

print(10 * name)

print(len(name))
print(name.lower())
print(last_name.upper())

print(name.strip())

# Espacio de memoria

a = [1,2,3,4,5]
b=a
print(b)

print(a)
print(b)
del a[0]
print(a)
print(id(a))
print(id(b))

c = a[:]
print(c)

a.append(7)
print(a)

