#88722959

def broken_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = nums[mid]
        if guess == target:
            return mid

        if guess > target:
                right = mid - 1

        else:
                left = mid + 1

        if nums[mid] >= nums[right]:
                left = mid + 1
        else:
                right = mid
    return right if right else len(arr) - 1 


if __name__ == "__main__":
    target = int(input())
    arr = [int(symbol) for symbol in input().strip().split()]
    print(broken_search(arr, target))