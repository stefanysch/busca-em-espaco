from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        stack = [initial]
        best_cost = {initial: 0}  # menor profundidade em que cada estado foi gerado
        expanded, generated, max_frontier = 0, 1, 1

        while stack:
            node = stack.pop()
            if node.is_goal:
                return SearchResult(node, expanded, generated, max_frontier, node.cost)
            if node.cost >= self.depth_limit:
                continue
            expanded += 1
            for child in node.neighbors():
                if child not in best_cost or child.cost < best_cost[child]:
                    best_cost[child] = child.cost
                    stack.append(child)
                    generated += 1
            max_frontier = max(max_frontier, len(stack))

        return SearchResult(None, expanded, generated, max_frontier)
