import math


N = 100


def new_pos(old_pos: int, move: str) -> int:
    direction = move[0]
    distance = int(move[1:])
    if direction == "L":
        return (old_pos - distance) % N
    elif direction == "R":
        return (old_pos + distance) % N
    else:
        raise ValueError(f"Invalid move direction: {direction}")


def solve(moves: list[str]) -> int:
    pos = 50
    score = 0
    for move in moves:
        pos = new_pos(pos, move)
        if pos == 0:
            score += 1
    return score


def solve2(moves: list[str]) -> int:
    pos = 50
    score = 0
    for move in moves:
        direction = move[0]
        distance = int(move[1:])
        if direction == "L":
            next_pos = (pos - distance) % N
        elif direction == "R":
            next_pos = (pos + distance) % N
        else:
            raise ValueError(f"Invalid move direction: {direction}")

        score += distance // N
        offset = distance % N
        if next_pos == 0:
            score += 1
        elif pos != 0 and direction == "L" and offset > pos:
            score += 1
        elif pos != 0 and direction == "R" and offset > (N - pos):
            score += 1
        # print(pos, move, next_pos, score)
        pos = next_pos
    return score


if __name__ == "__main__":
    with open("day01_test.txt") as f:
        test_input = f.read().splitlines()
    assert solve(test_input) == 3
    with open("day01_input.txt") as f:
        input_data = f.read().splitlines()
    print(solve(input_data))
    with open("day01_test.txt") as f:
        test_input = f.read().splitlines()
    assert solve2(test_input) == 6
    with open("day01_input.txt") as f:
        input_data = f.read().splitlines()
    print(solve2(input_data))
