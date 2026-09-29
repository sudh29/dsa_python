"""Tests for 12_graph/ — BFS, DFS, Dijkstra, Floyd-Warshall, Topological Sort."""

import importlib
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    """Dynamically imports a module from 12_graph/."""
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "12_graph" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestFloydWarshall:
    def test_basic(self):
        mod = _load("15_Floyd_Warshall_all_pairs_shortest_path.py")
        edges = [(0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1)]
        result = mod.floyd_warshall(4, edges)
        assert result[0][1] == 5
        assert result[0][2] == 8  # 0→1→2
        assert result[0][3] == 9  # 0→1→2→3

    def test_disconnected(self):
        mod = _load("15_Floyd_Warshall_all_pairs_shortest_path.py")
        edges = [(0, 1, 5)]
        result = mod.floyd_warshall(3, edges)
        assert result[0][1] == 5
        assert result[0][2] == float("inf")
        assert result[1][0] == float("inf")


class TestBFSAdjacencyMatrix:
    def test_basic(self):
        mod = _load("20_BFS_Adjacency_Matrix.py")
        g = mod.AdjacencyMatrixGraph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        result = g.bfs(0)
        assert result == [0, 1, 2, 3]

    def test_single_vertex(self):
        mod = _load("20_BFS_Adjacency_Matrix.py")
        g = mod.AdjacencyMatrixGraph(1)
        assert g.bfs(0) == [0]


class TestIterativeDFSBFS:
    def test_bfs_visits_all(self):
        mod = _load("21_Iterative_DFS_BFS_Stack.py")
        graph = {
            "0": {"1", "2"},
            "1": {"0", "3"},
            "2": {"0", "3"},
            "3": {"1", "2"},
        }
        result = mod.bfs_iterative(graph, "0")
        assert set(result) == {"0", "1", "2", "3"}
        assert result[0] == "0"

    def test_dfs_visits_all(self):
        mod = _load("21_Iterative_DFS_BFS_Stack.py")
        graph = {
            "0": {"1", "2"},
            "1": {"0", "3"},
            "2": {"0", "3"},
            "3": {"1", "2"},
        }
        result = mod.dfs_iterative(graph, "0")
        assert set(result) == {"0", "1", "2", "3"}
        assert result[0] == "0"


class TestAdjacencyDictGraph:
    def test_neighbors(self):
        mod = _load("22_Graph_Adjacency_Dict_Representation.py")
        g = mod.AdjacencyDictGraph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        assert g.get_neighbors(0) == [1, 2]

    def test_vertices(self):
        mod = _load("22_Graph_Adjacency_Dict_Representation.py")
        g = mod.AdjacencyDictGraph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        assert g.vertices() == {0, 1, 2}


class TestDijkstra:
    def test_basic_shortest_paths(self):
        mod = _load("12_Dijkstra_algo.py")
        sol = mod.Solution()
        v = 3
        adj = [[[1, 1], [2, 6]], [[0, 1], [2, 2]], [[1, 2], [0, 6]]]
        res = sol.dijkstra(v, adj, 0)
        assert res == [0, 1, 3]


class TestTopologicalSort:
    def test_dag_ordering(self):
        mod = _load("13_Implement_Topological_Sort.py")
        sol = mod.Solution()
        n = 6
        adj = [[], [], [3], [1], [0, 1], [0, 2]]
        res = sol.topoSort(n, adj)
        assert len(res) == n
        assert mod.check(adj, n, res) is True
