grafo = {}
grafo['inicio']={}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 2
# Aqui tem o primeiro vertice que chamamos de inicio,nele colocamos os dois vizinhos e dentro do vizinho seus custos

grafo['a']={}
grafo['a']['fim'] = 1
#Aqui colocamos os vizinhos e seus valores dos dois vertices vizinhos anteriores

grafo['b']={}
grafo['b']['a'] = 3
grafo['b']['fim'] = 5

grafo['fim']={} # vertice final nao tem vizinhos
print(grafo['b'])
print(grafo['a'])
infinito = float('inf')
custos = {}
custos['a'] = 6              # Aqui fizemos outro dicionario com os valores de cada vertice
custos['b'] = 2              # e uma variavel para representar o infinito
custos['fim'] = infinito

pais={}
pais['a'] = 'inicio'
pais['b'] = 'inicio'   # Criamos um outro dicionario para referenciar a origem dos registros
pais['fim'] =  None

processados = []   # E aqui guardamos os registros que ja foram processados para nao repetir a pesquisa

def ache_menor_custo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo
nodo = ache_menor_custo(custos)  # seleciona o mais barato a partir do inicio
while nodo is not None:    # cria um ciclo ate que chega ao fim ( fim == None linha 27)
    custo = custos[nodo]   # pega o custo desse mais barato (b)
    vizinhos = grafo[nodo]   # pega os vizinhos do b
    for n in vizinhos.keys():   # para cada vizinho :
        novo_custo = custo +vizinhos[n]   # soma o custo do b com cada um dos vizinhos
        if custos[n] > novo_custo:    # se o custo da soma for menor do que o custo original de ir ate o vizinho
            custos[n] = novo_custo    # a partir do inicio, mudamos o valor do vizinho (a)
            pais[n] = nodo            # e tomamos o (b) como o novo incio
    processados.append(nodo)          # coloca o caminho antigo (inicio) como ja processado
    print(nodo)
    print(custo[nodo])
    nodo = ache_menor_custo(custos) # recomeça o ciclo ate chegar a nulo
