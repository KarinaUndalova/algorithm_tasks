#88678367

def binary_search(arr, target, left=None, right=None):
    left = 0 if left is None else left
    right = len(arr) - 1 if right is None else right

    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def find_pivot(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= arr[right]:
            left = mid + 1
        else:
            right = mid
    return right if right else len(arr) - 1


def broken_search(nums, target):
    pivot = find_pivot(nums)

    if nums[pivot] == target:
        return pivot

    return binary_search(nums, target, right=pivot-1) if nums[0] <= target else binary_search(nums, target, left=pivot+1)


if __name__ == "__main__":
    target = int(input())
    arr = [int(symbol) for symbol in input().strip().split()]
    print(broken_search(arr, target))