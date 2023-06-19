# #id 88364317

def trainer(*, keys):
    scores = 0
    numbers = [0] * 10
    for row in range(4):
        for k in input():
            if k != '.':
                numbers[int(k)] += 1
    for k in numbers:
        scores += 1 if 0 < k <= 2 * keys else 0
    return scores


keys = int(input())

print(trainer(keys=keys))
