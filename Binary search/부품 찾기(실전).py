def binary_search(data, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


n = int(input())
data = list(map(int, input().split()))
data.sort()
m = int(input())
rq_data = list(map(int, input().split()))

for target in rq_data:
    result = binary_search(data, target, 0, n - 1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')

'''문제
1. 동빈이네 전자 매장에는 부품이 N개가 있다(각 부품은 정수 형태의 고유한 번호가 있다)
2. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 견적서를 요청했다.
3. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성'''