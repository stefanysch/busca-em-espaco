import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        """Distância de Manhattan de cada peça até sua posição final."""
        total = 0
        for i, tile in enumerate(state.tiles):
            if tile != 0:
                goal = GOAL_STATE.index(tile)
                total += abs(i // 3 - goal // 3) + abs(i % 3 - goal % 3)
        return total

    def search(self, initial: State) -> SearchResult:
        counter = 0  # desempate para o heap nunca comparar estados
        frontier = [(self.heuristic(initial), counter, initial)]
        closed = set()
        expanded, generated, max_frontier = 0, 1, 1

        while frontier:
            _, _, node = heapq.heappop(frontier)
            if node.is_goal:
                return SearchResult(node, expanded, generated, max_frontier, node.cost)
            if node in closed:
                continue
            closed.add(node)
            expanded += 1
            for child in node.neighbors():
                if child not in closed:
                    counter += 1
                    heapq.heappush(frontier, (child.cost + self.heuristic(child), counter, child))
                    generated += 1
            max_frontier = max(max_frontier, len(frontier))

        return SearchResult(None, expanded, generated, max_frontier)
