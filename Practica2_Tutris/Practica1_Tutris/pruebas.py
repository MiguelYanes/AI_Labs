from pieces import *
from state import *
from search import *

def sumar_array(array, x, y):
    # print "Antes: "
    # print array
    # print "x: " + str(x) + "   y: " + str(y)
    lenArray=len(array)
    nuevoArray=[]
    while len(array) is not 0 :
        pos=array.pop(0)
        pos0=pos[0]+x
        pos1=pos[1]+y
        nuevoArray.insert(lenArray, (pos0, pos1)) # inserta al final
    # print "Despues: "
    # print nuevoArray
    return nuevoArray
"""
piezaCubo = PieceSquare()
print piezaCubo.shape

piezaCubo.x=1
piezaCubo.y=2

print piezaCubo.occupied_positions()
print piezaCubo.shape
print piezaCubo.__str__()
piezaCubo.apply_movement('DOWN')
print piezaCubo.__str__()
"""

# 9.56 7 309 380 con comprobacion al expandir y con if
# 7.22 7 228 307 con comprobacion al generar  y con if
# 6.77 7 228 307 con comprobacion al generar  y sin if

# 1.53 29 62 133
# 1.60 29 61 132
# 1.52 29 31 132

# 8.86 7 288 377
# 6.58 7 221 328
# 6.37 7 221 328

piezaL = PieceL()
piezaL.x=1
piezaL.y=3
piezaS = PieceS()
piezaS.x=4
piezaS.y=6
piezaBarra = PieceBar()
piezaBarra.x=1
piezaBarra.y=7
piezaCubo = PieceSquare()
piezaCubo.x=0
piezaCubo.y=4

lista_piezas = [piezaL, piezaS, piezaBarra, piezaCubo]
#print lista_piezas

estado = TutrisState(lista_piezas)
estado.__str__()
accion=(1,'DOWN')
estado.successor(accion)
#print estado.is_valid()
#print estado.next_states()

#print "----------------------------------------"

busqueda = Node(estado, None, None)

piezaL = PieceL()
piezaL.x=0
piezaL.y=5
piezaS = PieceS()
piezaS.x=5
piezaS.y=6
piezaBarra = PieceBar()
piezaBarra.x=2
piezaBarra.y=6
piezaCubo = PieceSquare()
piezaCubo.x=1#0 CAMBIAR
piezaCubo.y=6

lista_piezas2 = [piezaL, piezaS, piezaBarra, piezaCubo]
#print lista_piezas2

estado2 = TutrisState(lista_piezas2)

#print "************************************"

estados=[]
estados.append(estado)
pruebas = PriorityQueue(lambda Pieza: Pieza.x);
pruebas.insert(piezaCubo)
pruebas.insert(piezaL)
pruebas.insert(piezaBarra)
print pruebas.remove().__str__()
pruebas.insert(piezaS)
print pruebas.remove().__str__()
print pruebas.remove().__str__()
print pruebas.remove().__str__()
#L C B S

#cola = PriorityQueue(lambda estado: estado.)


#print h1(estado, estado2)

#print uniform_cost(estado, estado2) #572 2876
#print breadth_first(estado, estado2) #572 2876
#a-star h1 3161
print depth_first(estado, estado2) #572 2876



"""
for i in range(4):
    print "i " + str(i)
    for j in range(5):
        print "j "+str(j)
        print "i j " + str((i,j))
"""

"""
par=(1,0)
asd=[(1,1),(0,1)]
contador=0
for i in range(4):
    forma=lista_piezas[i].shape
    if par in forma:
        print "si"
        contador = contador + 1
print contador

print forma
print par
"""

"""
arrayy=[(1,2),(1,3),(1,4)]
xx=1
yy=2
print sumar_array(arrayy, xx, yy);
"""

"""
array = [(1,(2, "1")),(2, (3, "j")),(5,(4, "w"))]

print array
for i in range(len(array)):
    print (array[i])[1]

print "----------"

for accion in array:
    print accion[1]
"""