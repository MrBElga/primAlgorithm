import heapq
import random

def ler_arquivo(filename):
    with open(filename, 'r') as file:
        linhas = file.readlines()

    #
    primeira_linha = linhas[0].strip()
    if primeira_linha[0].isalpha():  
   
        matriz_adjacencia = []
        for linha in linhas[1:]: 
            matriz_adjacencia.append(list(map(int, linha.split())))

        n = len(matriz_adjacencia)
        adj_list = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if matriz_adjacencia[i][j] != 0:
                    adj_list[i].append((j, matriz_adjacencia[i][j]))

        return n, adj_list
    else:

        n, m = map(int, primeira_linha.split()) 
        adj_list = [[] for _ in range(n)]
        for linha in linhas[1:]:
            origem, destino, custo = map(int, linha.split())
            adj_list[origem].append((destino, custo))
            adj_list[destino].append((origem, custo))  

        return n, adj_list

def prim(n, n_out):
    raiz = random.randint(0, n - 1)
    H = []

    for (x, c) in n_out[raiz]: 
        heapq.heappush(H, (c, raiz, x)) 

    marcados = [False] * n
    marcados[raiz] = True 

    n_edge = 0 
    custo_tot = 0 
    arv_ger_mim = [] 

    print(f"\nIniciando o algoritmo a partir da raiz: {raiz}\n")
    cont = 0
    while n_edge < n - 1: 
        while True: 
            c, a, b = heapq.heappop(H) 
            if not marcados[b]:
                break
   
        print(f"\nAnalisando aresta: {a} --({c})--> {b}")
        print("Vértices marcados: ", ["X" if marcados[i] else str(i) for i in range(n)]) 


        marcados[b] = True 
        custo_tot += c 
        print(f"\n###### RESULTADOS ({cont}) ######")
        cont +=1 
        arv_ger_mim.append((a, b))
        n_edge += 1 

        for (x, c) in n_out[b]: 
            if not marcados[x]: 
                heapq.heappush(H, (c, b, x)) 

        print("\n### HEAP ###")
        print(H)
    print(f"\nCusto Total da Árvore Geradora Mínima: {custo_tot}\n")
    
    print("Arestas da Árvore Geradora Mínima:")
    for a, b in arv_ger_mim:
        print(f" - {a} -- {b}")
    
    print("\n###### FIM DOS RESULTADOS ######\n")


def imprimir_lista_adjacencia(n_out):
    print("\n### Lista de Adjacência ###")
    for a, b in enumerate(n_out):
        print(f"Vértice {a} -> {b}")

print("Digite o nome do arquivo de entrada:") 
filename = input()  
n, n_out = ler_arquivo(filename) 
imprimir_lista_adjacencia(n_out)
prim(n, n_out)
