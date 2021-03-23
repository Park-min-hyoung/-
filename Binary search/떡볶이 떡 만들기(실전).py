from sys import stdin

def binary_search(rice, start, end):
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in rice:
            if i > mid:
                cnt += (i - mid)

        # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
        if cnt >= m:
            start = mid + 1
            res = mid
        # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
        else:
            end = mid - 1

    return res


n, m = map(int, stdin.readline().split())
rice = list(map(int, stdin.readline().split()))

print(binary_search(rice, 0, max(rice)))

'''문제
1. 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
(잘린 떡의 길이는 차례대로 4, 0, 0, 2cm => 손님은 6cm 만큼의 떡을 가진다)
2. 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성
'''
