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

    print(f"\nIniciando o algoritmo a partir da raiz: {raiz}\n")

    while n_edge < n - 1: # Enquanto não tiver n - 1 arestas
        while True: # Enquanto não encontrar uma aresta válida
            c, a, b = heapq.heappop(H) # Remove a aresta de menor custo
            if not marcados[b]: # Se o vértice b não foi marcado
                break # Sai do loop
        # Aresta analisada
        print(f"\nAnalisando aresta: {a} --({c})--> {b}")
        print("Vértices marcados: ", ["X" if marcados[i] else str(i) for i in range(n)])


        marcados[b] = True # Marca o vértice b
        custo_tot += c # Incrementa o custo total
    print("\n###### RESULTADOS ######")
        arv_ger_mim.append((a, b)) # Adiciona a aresta na árvore geradora mínima
        n_edge += 1 # Incrementa o número de arestas

        for (x, c) in n_out[b]: # Para cada aresta (x, c) que sai de b
            if not marcados[x]: # Se o vértice não foi marcado
                heapq.heappush(H, (c, b, x)) # Adiciona a aresta na heap


    # Exibe o custo total e a árvore geradora mínima de forma formatada
    print(f"Custo Total da Árvore Geradora Mínima: {custo_tot}\n")
    
    print("Arestas da Árvore Geradora Mínima:")
    for a, b in arv_ger_mim:
        print(f" - {a} -- {b}")
    
    print("\n###### FIM DOS RESULTADOS ######\n")

print("Digite o nome do arquivo de entrada:") # Pede o nome do arquivo de entrada
filename = input()  
n, n_out = ler_arquivo(filename) # Lê o arquivo de entrada
prim(n, n_out) # Executa o algoritmo de Prim
