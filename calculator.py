#88460392

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise IndexError('Нет операндов для расчета.')


def calculator(line):
    stack = Stack()
    for element in line:
        if element in OPERATORS:
            operand1, operand2 = stack.pop(), stack.pop()
            try:
                stack.push(int(OPERATORS[element](operand2, operand1)))
            except ZeroDivisionError:
                raise ZeroDivisionError('Ошибка деления на ноль.')
            except TypeError:
                raise TypeError(f'{element} операция не поддерживается.')
        else:
            try:
                stack.push(int(element))
            except:
                raise KeyError(f'Невозможно преобразовать {element}')
    return stack.pop()


if __name__ == '__main__':
    inp_string = input().split()
    print(calculator(inp_string))
