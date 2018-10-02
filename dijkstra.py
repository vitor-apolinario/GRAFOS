class Vertice:
    def __init__(self,nome,visitado):
        self.nome=nome
        self.visitado=visitado
        self.vant=None
        self.vizinhos=[]
        self.custo=5000

class Aresta:
    def __init__(self, nome, custo, a, b):
        self.nome=nome
        self.custo=custo
        self.vertices=[a,b]

class Caminho:
    def __init__(self, vertice, custo):
        self.vertice=vertice
        self.custo=custo

def descobre_arestas(atual,arestas,abertos):
    caminhos=[]
    for x in arestas:
        if x.vertices.__contains__(atual):
            for y in x.vertices:
                if y!=atual and abertos.__contains__(y):
                    caminhos.append(Caminho(y, x.custo))
    return caminhos

a=Vertice('a',False)
b=Vertice('b',False)
c=Vertice('c',False)
d=Vertice('d',False)

arestas=[
    Aresta('a1', 6, a, c),
    Aresta('a2', 4, a, b),
    Aresta('a3', 1, b, c),
    Aresta('a4', 3, b, d),
    Aresta('a5', 4, c, d)
]

abertos=[a, b, c, d]

grafo={
    'a': a,
    'b': b,
    'c': c,
    'd': d
}

atual=grafo[input('Digite o vértice inicial: ')]
nf=grafo[input('Digite o vértice final: ')]
atual.custo=0
abertos.remove(atual)

while True:
    caminhos=descobre_arestas(atual,arestas,abertos)
    print(atual.nome)
    for x in caminhos:
        print('custo novo:{} custo antigo:{}'.format(x.custo + atual.custo, x.vertice.custo),end=' ')
        if x.custo+atual.custo < x.vertice.custo:
            print('troca')
            x.vertice.custo = x.custo+atual.custo
            x.vertice.vant = atual
        else:
            print('não troca')

    if atual.custo:
        abertos.remove(atual)

    #acha o próximo vértice (menor custo)
    if abertos:
        m=5000
        n='vazio'
        for x in abertos:
            if x.custo < m:
                m=x.custo
                n=x.nome
        atual=grafo[n]
    else:
        break

#backtracking
while nf:
    print('vértice:{} custo:{} anterior:{}'.format(nf.nome,nf.custo,nf.vant.nome if nf.vant else 'none'))
    nf = nf.vant
