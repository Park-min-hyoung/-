from sys import stdin

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return array[start:end + 1].count(target)
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


n, target = map(int, stdin.readline().split())
array = list(map(int, stdin.readline().split()))

res = binary_search(array, target, 0, n - 1)

if res == None:
    print(-1)
else:
    print(res)