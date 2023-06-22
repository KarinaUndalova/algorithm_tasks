#88460578

ERROR_MESSAGE = 'error'
ERROR_COMMAND = 'Error in command: {command}'


class Deque:
    def __init__(self, max_size):
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def __check_full_queue(self):
        return self.__size == self.__max_size

    def __check_empty_queue(self):
        return self.__size == 0

    def __get_index(self, method):
        if method == 'push_front':
            if self.__check_empty_queue():
                self.__head = 0
                self.__tail = 0
                return 0
            return (self.__head - 1) % self.__max_size
        if method == 'push_back':
            if self.__check_empty_queue():
                self.__head = 0
                self.__tail = 0
                return 0
            return (self.__tail + 1) % self.__max_size
        if method == 'pop_front':
            return (self.__head + 1) % self.__max_size
        if method == 'pop_back':
            return (self.__tail - 1) % self.__max_size

    def push_front(self, value):
        """Метод push_front добавляет элемент в начало дека"""
        if self.__check_full_queue():
            raise RuntimeError(ERROR_MESSAGE)
        self.__head = self.__get_index('push_front')
        self.__items[self.__head] = value
        self.__size += 1

    def push_back(self, value):
        """Метод push_back добавляет элемент в конец дека"""
        if self.__check_full_queue():
            raise RuntimeError(ERROR_MESSAGE)
        self.__tail = self.__get_index('push_back')
        self.__items[self.__tail] = value
        self.__size += 1

    def pop_front(self):
        """Метод pop_front удаляет элемент из начала дека и возвращает его"""
        if self.__check_empty_queue():
            raise RuntimeError(ERROR_MESSAGE)
        value = self.__items[self.__head]
        self.__head = self.__get_index('pop_front')
        self.__size -= 1
        return value

    def pop_back(self):
        """Метод pop_back удаляет элемент из конца дека и возвращает его"""
        if self.__check_empty_queue():
            raise RuntimeError(ERROR_MESSAGE)
        value = self.__items[self.__tail]
        self.__tail = self.__get_index('pop_back')
        self.__size -= 1
        return value


if __name__ == '__main__':
    command_count = int(input())
    deque = Deque(max_size=int(input()))
    for _ in range(command_count):
        try:
            command, *params = input().strip().split(' ')
            result = getattr(deque, command)(*params)
            if 'pop' in command:
                print(result)
        except RuntimeError:
            print(ERROR_MESSAGE)
        except AttributeError:
            raise ValueError(ERROR_COMMAND.format(command=command))
