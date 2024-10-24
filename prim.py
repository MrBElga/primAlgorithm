import heapq
import random

def ler_arquivo(filename):
    with open(filename, 'r') as file:
        linhas = file.readlines() # Lê as linhas do arquivo
    
    n, m = map(int, linhas[0].split()) # Número de vértices e arestas
    n_out = [[] for _ in range(n)] # Lista de adjacência
    
    for linha in linhas[1:]: # Para cada linha do arquivo
        a, b, c = map(int, linha.split()) # Vértice de origem, vértice de destino e custo
        n_out[a].append((b, c)) # Adiciona a aresta na lista de adjacência
        n_out[b].append((a, c)) # Adiciona a aresta na lista de adjacência
    
    return n, n_out

def prim(n, n_out):
    raiz = random.randint(0, n - 1) # Vértice raiz
    H = [] # Heap

    for (x, c) in n_out[raiz]: # Para cada aresta (x, c) que sai da raiz
        heapq.heappush(H, (c, raiz, x)) # Adiciona as arestas que saem da raiz na heap

    marcados = [False] * n # Vértices marcados
    marcados[raiz] = True  # Marca o vértice raiz

    n_edge = 0 # Número de arestas
    custo_tot = 0 # Custo total
    arv_ger_mim = [] # Árvore geradora mínima

    while n_edge < n - 1: # Enquanto não tiver n - 1 arestas
        while True: # Enquanto não encontrar uma aresta válida
            c, a, b = heapq.heappop(H) # Remove a aresta de menor custo
            if not marcados[b]: # Se o vértice b não foi marcado
                break # Sai do loop

        print(a,b) # Imprime a aresta que está sendo analisada
        print("###### marcados ######\n" + str(marcados) + "\n") # Imprime os vértices marcados

        marcados[b] = True # Marca o vértice b
        custo_tot += c # Incrementa o custo total
        arv_ger_mim.append((a, b)) # Adiciona a aresta na árvore geradora mínima
        n_edge += 1 # Incrementa o número de arestas

        for (x, c) in n_out[b]: # Para cada aresta (x, c) que sai de b
            if not marcados[x]: # Se o vértice não foi marcado
                heapq.heappush(H, (c, b, x)) # Adiciona a aresta na heap


    print("###### Custo Total ######\n" + str(custo_tot) + "\n")  # Imprime o custo total
    print("###### Árvore Geradora Mínima ######\n" + str(arv_ger_mim) + "\n") # Imprime a árvore geradora mínima

print("Digite o nome do arquivo de entrada:") # Pede o nome do arquivo de entrada
filename = input()  
n, n_out = ler_arquivo(filename) # Lê o arquivo de entrada
prim(n, n_out) # Executa o algoritmo de Prim
