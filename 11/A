#id 87598822
def data_input():
    length_street = int(input())
    street = [int(num) for num in input().split(' ')]
    return length_street, street
def calculations():
    length_street, street = data_input()
    distance = []
    zero_position = None
    for index, elem in enumerate(street):
        if elem == 0:
            zero_position = index
            distance.append(0)
            continue
        if (elem != 0 and zero_position != None):
            distance.append(i - zero_position)
        else:
            distance.append(length_street)
    zero_position = None
    for index, elem in reversed(list(enumerate(street))):
        if elem == 0:
            zero_position = i
            continue
        if (elem != 0 and zero_position != None and distance[index] > zero_position - index):
            distance[i] = (zero_position - i)
    print(*distance)
if __name__ == '__main__':
    calculations()
