# 8-Puzzle — Busca em Espaço de Estados

Implementação de três algoritmos clássicos de busca aplicados ao problema do 8-puzzle: **BFS** (Busca em Largura), **DFS** (Busca em Profundidade) e **A*** (com heurística de Manhattan).

## Como rodar

```bash
python main.py
```

Requer Python 3.10+.

## O que foi implementado

### `puzzle/state.py`
- `neighbors()` — gera os estados filhos a partir do espaço vazio
- `path()` — reconstrói a sequência de estados do inicial até este
- `actions()` — retorna a sequência de ações usando `path()`

### `algorithms/bfs.py`
- `BFS.search(initial)` — Busca em Largura (encontra a solução mais curta)

### `algorithms/dfs.py`
- `DFS.search(initial)` — Busca em Profundidade com limite de profundidade 50

### `algorithms/a_star.py`
- `AStar.heuristic(state)` — Distância de Manhattan (admissível)
- `AStar.search(initial)` — Busca A* (combina custo + heurística)

## Estrutura

```
├── puzzle/
│   ├── state.py        # State — neighbors, path, actions
│   ├── result.py       # SearchResult — não alterar
│   └── base_search.py  # Interface BaseSearch — não alterar
├── algorithms/
│   ├── bfs.py          # BFS
│   ├── dfs.py          # DFS
│   └── a_star.py       # A*
└── main.py             # Demo dos algoritmos
```

## Resultados esperados

Ao rodar `python main.py`, você verá para cada algoritmo:
- **Solução**: sequência de movimentos (cima, baixo, esquerda, direita)
- **Custo**: número de movimentos
- **Nós expandidos**: quantos estados foram analisados
- **Fronteira máxima**: maior tamanho da fila/pilha/heap durante a busca

BFS e A* encontram a solução ótima com custo idêntico. DFS pode encontrar uma solução mais longa.

