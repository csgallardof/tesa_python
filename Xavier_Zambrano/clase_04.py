
##### matrices

matriz = [1,2,3,4]
print(matriz)

matriz2d = [['r','r','r','r'],[1,2,3,4]]
print(matriz2d)


tablero_ajedrez = [['T','A','C','R','RY','C','A','T'],
                   ['P','P','P','P','P','P','P','P'],
                   ['0','0','0','0','0','0','0','0'],
                   ['0','0','0','0','0','0','0','0'],
                   ['0','0','0','0','0','0','0','0'],
                   ['0','0','0','0','0','0','0','0'],
                   ['P','P','P','P','P','P','P','P'],
                   ['T','A','C','R','RY','C','A','T'],
                   ]

print(tablero_ajedrez)

for fila in tablero_ajedrez:
    print(fila,"\n")

print (tablero_ajedrez[7][3]) ## posicion de matrices de X y Y
print (tablero_ajedrez[0][0]) ## posicion de matrices de X y Y



    