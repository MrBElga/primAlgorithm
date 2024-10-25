## Algoritmo de Prim - Árvore Geradora Mínima (AGM)

Este projeto implementa o **Algoritmo de Prim** para encontrar a **Árvore Geradora Mínima** de um grafo não direcionado. O grafo é lido a partir de um arquivo texto, e a saída inclui o custo total e a árvore geradora mínima.

## 📜 Descrição

O **Algoritmo de Prim** é um método guloso utilizado para encontrar a árvore geradora mínima de um grafo. Ele funciona expandindo uma árvore a partir de um vértice inicial, conectando-a aos vértices ainda não incluídos, sempre escolhendo a aresta de menor peso.

### ⚙️ Funcionamento do Algoritmo

1. **Entrada**:
    - Um arquivo texto contendo:
      - O número de vértices `n` e o número de arestas `m`.
      - Uma lista de arestas, cada uma no formato: `vértice1 vértice2 peso`.
2. **Saída**:
    - O **custo total** da árvore geradora mínima.
    - A **lista de arestas** que compõem a árvore geradora mínima.

### 📥 Exemplo de Entrada

Arquivo `grafo1.txt`:
5 7 
0 1 2 
0 3 6 
1 2 3 
1 3 8 
1 4 5 
2 4 7 
3 4 9

shell
Copiar código

### 📤 Exemplo de Saída

Custo Total
16

Árvore Geradora Mínima
[(0, 1), (1, 2), (1, 4), (0, 3)]

markdown
Copiar código

## 🚀 Execução

### Pré-requisitos

- Python 3.x instalado.

### Instruções

1. Clone o repositório ou faça o download do código.
2. Crie um arquivo texto de entrada com o formato especificado.
3. No terminal, execute o script da seguinte forma:

```bash
python prim.py
```

Quando solicitado, insira o nome do arquivo de entrada (ex: grafo1.txt).
Estrutura de Arquivos
bash
Copiar código

├── prim.py        # Script principal contendo o algoritmo de Prim
├── grafo1.txt     # Exemplo de arquivo de entrada
├── LICENSE.md     # Licensa do MIT
└── README.md      # Este arquivo

## 🛠️ Explicação do Código
ler_arquivo(filename): Lê o arquivo de entrada e converte-o em uma lista de adjacência para ser usada no algoritmo.
prim(n, n_out): Executa o algoritmo de Prim, utilizando uma fila de prioridade para selecionar as arestas de menor peso.
heapq: Utilizado para gerenciar a fila de prioridade de maneira eficiente.

## 💡 Exemplo de Uso

Considere o seguinte grafo com 5 vértices e 7 arestas. A partir dele, o algoritmo de Prim encontra a árvore geradora mínima com um custo total de 16.

    2       3
0 ------ 1 ----- 2
|       / |       \
6      8  5        7
|     /   |         \
3 -- 4 ----          9

Grafo de Entrada (grafo1.txt)
```shell
Copiar código
5 7
0 1 2
0 3 6
1 2 3
1 3 8
1 4 5
2 4 7
3 4 9
Saída
```

saida
###### Custo Total ######
16

###### Árvore Geradora Mínima ######
[(0, 1), (1, 2), (1, 4), (0, 3)]
