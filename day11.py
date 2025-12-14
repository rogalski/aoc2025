import functools
import json


def solve(file_path: str) -> int:
    partitioned = [line.partition(": ") for line in open(file_path).readlines()]
    graph = {
        label.strip(): set(connections.strip().split())
        for label, _, connections in partitioned
    }
    return sum(1 for p in dfs("you", "out", graph))


def solve2(file_path: str) -> int:
    partitioned = [line.partition(": ") for line in open(file_path).readlines()]
    graph = {
        label.strip(): sorted(connections.strip().split())
        for label, _, connections in partitioned
    }
    graph_json = json.dumps(graph)
    svr_dac_paths = dfs_count("svr", "dac", graph_json)
    svr_fft_paths = dfs_count("svr", "fft", graph_json)
    dac_fft_paths = dfs_count("dac", "fft", graph_json)
    fft_dac_paths = dfs_count("fft", "dac", graph_json)
    dac_out_paths = dfs_count("dac", "out", graph_json)
    fft_out_paths = dfs_count("fft", "out", graph_json)
    return (
        0
        + svr_dac_paths * dac_fft_paths * fft_out_paths
        + svr_fft_paths * fft_dac_paths * dac_out_paths
    )


def dfs(
    start_node: str,
    end_node: str,
    graph: dict[str, set[str]],
    path: list[str] = [],
):
    curr_path = path + [start_node]
    if start_node == end_node:
        yield curr_path
        return
    if start_node not in graph:
        return  # no more neighbors
    for neighbor in graph[start_node]:
        yield from dfs(neighbor, end_node, graph, curr_path)


@functools.cache
def dfs_count(start_node: str, end_node: str, graph_json: str) -> int:
    if start_node == end_node:
        return 1

    graph = json.loads(graph_json)

    if start_node not in graph:
        return 0  # dead end

    return sum(dfs_count(n, end_node, graph_json) for n in graph[start_node])


assert solve("day11_test.txt") == 5
print(solve("day11_input.txt"))
assert solve2("day11_test2.txt") == 2
print(solve2("day11_input.txt"))
