g = \
[[0, 0, 4, 1, 3, 0],
 [1, 0, 0, 5, 0, 5],
 [4, 0, 0, 0, 0, 0],
 [0, 5, 0, 1, 4, 2],
 [0, 3, 0, 3, 0, 1],
 [5, 1, 0, 0, 1, 0]]

def verticesN(g): # grafo -> int : devuelve la cantidad de vertices
  return len(g)
def aristasM(g): # grafo -> int : devuelve la cantidad de aristas
  cont = 0
  for i in range(len(g)):
    for j in range(len(g)):
      if g[i][j] != 0:
        cont += 1
  return cont
def vecinos(grafo,vertice): # grafo x vertice -> [vertices] : devuelve la lista de vecinos
  v = []
  for i in range(len(grafo)):
    if grafo[vertice][i] != 0:
      v.append(i)
  return v
def gradoMas(grafo,vertice): # grafo x vertice -> int
  v = []
  for i in range(len(grafo)):
    if grafo[vertice][i] != 0:
      v.append(i)
  mas = v
  return (len(mas))
def gradoMas(grafo,vertice): # grafo x vertice -> int
  pass
def esdirigido(g): # grafo -> Bool
  pass

assert verticesN(g) == 6
assert aristasM(g) == 17
assert vecinos(g,1)==[0,3,5]
assert gradoMas(g,1)==3
assert gradoMenos(g,3)==4
assert esdirigido(g) == True

g2 = [[0,3,2],
      [3,0,1],
      [2,1,0]]

assert esdirigido(g2)== False
