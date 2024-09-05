
print("\nStrings")

name = 'Pablo'
last_name = 'Miranda'

print(name + ' ' + last_name)

print('\nPablo has ' + str(len(name)) + ' characters')

print('\nArrays')

a = [1,2,3,4,5,6]
b = a

print(a)
print(b)


print('\nDeleting item at position: 2[#3]')
del a[2]

print(a)
print(b)

print('\nAdd item [8] at last position')
a.append(8)

print(b)