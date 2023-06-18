# 88329461

from typing import List


def trainer(number: int, matrix: List[str]) -> int:
    numbers = {}
    for i in range(1, 10):
        numbers[i] = 0

    scores = 0
    for i in range(4):
        for k in matrix[i]:
            if k == '.':
                continue
            numbers[int(k)] += 1
    for val in numbers.values():
        if 0 < val <= 2 * number:
            scores += 1
    numbers = {i: 0 for i in numbers}

    return scores


if __name__ == '__main__':
    number = int(input())
    matrix = [input() for i in range(4)]
    print(trainer(number, matrix))
