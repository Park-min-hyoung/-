from sys import stdin

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1


n = int(stdin.readline())
array = list(map(int, stdin.readline().split()))

res = binary_search(array, 0, n - 1)

if res == None:
    print(-1)
else:
    print(res)