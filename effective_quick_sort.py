#88749269

def quick_sort(users, length):

    def _quick_sort(users, left, right):
        if left < right:
            part = partition(users, left, right)
            _quick_sort(users, left, part)
            _quick_sort(users, part + 1, right)

    def partition(users, left, right):
        pivot = users[left]
        while True:
            while users[left] < pivot:
                left = left + 1
            while users[right] > pivot:
                right = right - 1
            if left >= right:
                return right
            users[left], users[right] = users[right], users[left]
            left = left + 1
            right = right - 1

    _quick_sort(users, 0, length - 1)
    return users


if __name__ == '__main__':
    length = int(input())
    users = []
    for _ in range(length):
        user_name, tasks_solved, failed_attempts = input().split()
        tasks_solved = int(tasks_solved)
        failed_attempts = int(failed_attempts)
        users.append([-tasks_solved, failed_attempts, user_name])
    quick_sort(users, length)
    print(*(list(zip(*users))[2]), sep="\n")
