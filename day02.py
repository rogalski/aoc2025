import math


def sum_invalid_ids(s: str) -> int:
    items = s.split(",")
    tuples = [(int(item.split("-")[0]), int(item.split("-")[1])) for item in items]
    invalid_sum = 0
    for a, b in tuples:
        for i in range(a, b + 1):
            istr = str(i)
            left = istr[: len(istr) // 2]
            right = istr[len(istr) // 2 :]
            if left == right:
                invalid_sum += i
    return invalid_sum


def sum_invalid_ids2(s: str) -> int:
    items = s.split(",")
    tuples = [(int(item.split("-")[0]), int(item.split("-")[1])) for item in items]
    invalid_sum = 0
    for a, b in tuples:
        for i in range(a, b + 1):
            istr = str(i)
            ilen = len(istr)
            for j in range(1, ilen // 2 + 1):
                if ilen % j == 0:
                    maybe_pieces = [istr[k : k + j] for k in range(0, ilen, j)]
                    if all(piece == maybe_pieces[0] for piece in maybe_pieces):
                        # print("invalid", i, maybe_pieces)
                        invalid_sum += i
                        break
    return invalid_sum


assert sum_invalid_ids(open("day02_test.txt").read()) == 1227775554
print(sum_invalid_ids(open("day02_input.txt").read()))
assert sum_invalid_ids2(open("day02_test.txt").read()) == 4174379265
print(sum_invalid_ids2(open("day02_input.txt").read()))
