matriz = [1,2,3,4]
print(matriz)
      
matriz2d = [ ['r','r','r','r'], [1,2,3,4]]

print(matriz2d)


##tablero de ajedrez

tablero_ajedrez = [['t','a','c','re','ra','c','a','t'],
                   ['p','p','p','p','p','p','p','p'],
                   ['0','0','0','0','0','0','0','0'],
                   ['0','0','0','0','0','0','0','0'],
                   ['0','0','0','0','0','0','0','0'],
                   ['0','0','0','0','0','0','0','0'],
                   ['p','p','p','p','p','p','p','p'],
                   ['t','a','c','re','ra','c','a','t']]

print(tablero_ajedrez)

for fila in tablero_ajedrez:
    print(fila,"\n")

##imprimir posiciones
print(tablero_ajedrez[5][0])
print(tablero_ajedrez[5][2])
print(tablero_ajedrez[6][3])
print(tablero_ajedrez[7][3])



