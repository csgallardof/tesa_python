### Matrices de datos

matriz = [1,2,3,4]
print(matriz)

### arreglo de arreglo

matriz2d = [('r','r','r','r',[1,2,3,4])]
print(matriz2d)


tablero_ajedrez=[['t', 'a', 'c', 'r', 'ra', 'c', 'a', 't'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                ['0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                ['t', 'a', 'c', 'r', 'ra', 'c', 'a', 't']
                ]

print(tablero_ajedrez)
print("\n")

for fila in tablero_ajedrez:
    print(fila,"\n")
    

print(tablero_ajedrez[0][0])
print(tablero_ajedrez[5][2])
print(tablero_ajedrez[3][4])


print("\n")