def distance(
    points1: list[tuple[int, int, int]], points2: list[tuple[int, int, int]]
) -> int:
    return min(
        (p1[2] - p2[2]) * (p1[2] - p2[2])
        + (p1[1] - p2[1]) * (p1[1] - p2[1])
        + (p1[0] - p2[0]) * (p1[0] - p2[0])
        for p1 in points1
        for p2 in points2
    )


def solve(file_path: str, iters: int) -> int:
    with open(file_path, "r") as file:
        points: list[tuple[int, int, int]] = [
            tuple(map(int, line.strip().split(","))) for line in file
        ]
    clusters = []
    distances = [
        (
            i1,
            i2,
            (p1[2] - p2[2]) * (p1[2] - p2[2])
            + (p1[1] - p2[1]) * (p1[1] - p2[1])
            + (p1[0] - p2[0]) * (p1[0] - p2[0]),
        )
        for i1, p1 in enumerate(points)
        for i2, p2 in enumerate(points)
        # do not count same point pairs twice
        if i1 < i2
    ]
    connections = 0
    for s in sorted(distances, key=lambda x: x[2]):
        first_index, second_index = s[0], s[1]
        first_index_cluster = None
        second_index_cluster = None
        for i, cluster in enumerate(clusters):
            if first_index in cluster:
                first_index_cluster = i
            if second_index in cluster:
                second_index_cluster = i
            if first_index_cluster is not None and second_index_cluster is not None:
                break

        if (
            first_index_cluster is not None
            and second_index_cluster is not None
            and first_index_cluster != second_index_cluster
        ):
            # merge clusters into first one
            clusters[first_index_cluster].update(clusters[second_index_cluster])
            clusters[second_index_cluster] = set()
        elif first_index_cluster is not None:
            clusters[first_index_cluster].add(second_index)
        elif second_index_cluster is not None:
            clusters[second_index_cluster].add(first_index)
        else:
            clusters.append({first_index, second_index})
        connections += 1
        if connections >= iters:
            break

    sorted_lengths = sorted([len(c) for c in clusters], reverse=True)
    return sorted_lengths[0] * sorted_lengths[1] * sorted_lengths[2]


def solve2(file_path: str) -> int:
    with open(file_path, "r") as file:
        points: list[tuple[int, int, int]] = [
            tuple(map(int, line.strip().split(","))) for line in file
        ]
    clusters = []
    distances = [
        (
            i1,
            i2,
            (p1[2] - p2[2]) * (p1[2] - p2[2])
            + (p1[1] - p2[1]) * (p1[1] - p2[1])
            + (p1[0] - p2[0]) * (p1[0] - p2[0]),
        )
        for i1, p1 in enumerate(points)
        for i2, p2 in enumerate(points)
        # do not count same point pairs twice
        if i1 < i2
    ]
    connections = 0
    for s in sorted(distances, key=lambda x: x[2]):
        first_index, second_index = s[0], s[1]
        first_index_cluster = None
        second_index_cluster = None
        for i, cluster in enumerate(clusters):
            if first_index in cluster:
                first_index_cluster = i
            if second_index in cluster:
                second_index_cluster = i
            if first_index_cluster is not None and second_index_cluster is not None:
                break

        if (
            first_index_cluster is not None
            and second_index_cluster is not None
            and first_index_cluster != second_index_cluster
        ):
            # merge clusters into first one
            clusters[first_index_cluster].update(clusters[second_index_cluster])
            del clusters[second_index_cluster]
        elif first_index_cluster is not None:
            clusters[first_index_cluster].add(second_index)
        elif second_index_cluster is not None:
            clusters[second_index_cluster].add(first_index)
        else:
            clusters.append({first_index, second_index})
        connections += 1
        if max(len(c) for c in clusters) == len(points):
            first_x = points[first_index][0]
            second_x = points[second_index][0]
            return first_x * second_x


assert solve("day08_test.txt", 10) == 40
print(solve("day08_input.txt", 1000))
print(solve2("day08_input.txt"))
