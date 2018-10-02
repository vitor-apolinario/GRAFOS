class Vertice:
    def __init__(self,nome,cor,dist):
        self.nome=nome
        self.cor=cor
        self.dist=dist
        self.vant=None
        self.vizinhos=[]

def visita_nodo(nodo, fila):
    for x in nodo.vizinhos:
        if x.cor=='b':
            x.cor='c'
            x.dist=(nodo.dist+1)
            x.vant=nodo
            fila.append(x)
            
def printa_nodo(nodo):
    print('vértice: {}, cor: {}, distancia: {}, anterior: {}'.format(nodo.nome, nodo.cor, nodo.dist, nodo.vant.nome if nodo.vant else "none"))

a = Vertice('a','b',0)
b = Vertice('b','b',0)
c = Vertice('c','b',0)
d = Vertice('d','b',0)
e = Vertice('e','b',0)
f = Vertice('f','b',0)
g = Vertice('g','b',0)
h = Vertice('h','b',0)
i = Vertice('i','b',0)
j = Vertice('j','b',0)
k = Vertice('k','b',0)
l = Vertice('l','b',0)
m = Vertice('m','b',0)
n = Vertice('n','b',0)
o = Vertice('o','b',0)
p = Vertice('p','b',0)
q = Vertice('q','b',0)
r = Vertice('r','b',0)
s = Vertice('s','b',0)
t = Vertice('t','b',0)
z = Vertice('z','b',0)


a.vizinhos=[b, k]
b.vizinhos=[a, c, d]
c.vizinhos=[b, e]
d.vizinhos=[b, e, l]
e.vizinhos=[c, d, f, g]
f.vizinhos=[e, h]
g.vizinhos=[e, i]
h.vizinhos=[f, i, j]
i.vizinhos=[g, h, j]
j.vizinhos=[h, i, z]
k.vizinhos=[a, l, m, n]
l.vizinhos=[d, k, o]
m.vizinhos=[k, o]
n.vizinhos=[k, o]
o.vizinhos=[l, m, n, p, r]
p.vizinhos=[o, q]
q.vizinhos=[p, r, s, t]
r.vizinhos=[o, q]
s.vizinhos=[q, z]
t.vizinhos=[q,z]
z.vizinhos=[j, s, t]

#dicionário
grafo={'a': a,
       'b': b,
       'c': c,
       'd': d,
       'e': e,
       'f': f,
       'g': g,
       'h': h,
       'i': i,
       'j': j,
       'k': k,
       'l': l,
       'm': m,
       'n': n,
       'o': o,
       'p': p,
       'q': q,
       'r': r,
       's': s,
       't': t,
       'z': z,}

fila=[]
fila.append(grafo[input('Digite o vértice inicial: ')])
nf=grafo[input('Digite o vértice final: ')]

while True:
    if fila:
        visita_nodo(fila[0],fila)
        fila[0].cor='p'
        fila.remove(fila[0])
    else:
        break

for i in grafo.keys():
    printa_nodo(grafo[i])

#backtracking
print('Caminho')
while True:
    print(nf.nome)
    nf = nf.vant
    if not nf:
        break


