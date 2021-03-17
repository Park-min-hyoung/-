def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 찾으려는 값보다 중간점 인덱스에 해당하는 값이 크다면 end 점을 이동
        elif array[mid] > target:
            end = mid - 1
        # 찾으려는 값돠 중간점 인덱스에 해당하는 값이 작다면 start 점을 이동
        else:
            start = mid + 1
    return None


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = map(int, input().split())
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)