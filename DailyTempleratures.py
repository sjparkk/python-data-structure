"""
문제
매일의 온도를 나타내는 int형 배열 temperatures가 주어진다. answer 배열의 원소 answer[i]는 i번 째 날의 온도보다 더 따뜻해지기까지 며칠을 기다려야하는지 나타낸다.
만약 더 따뜻해지는 날이 없다면 answer[i] == 0 이다. answer 배열을 반환하는 함수를 구현하라.

제약 조건
1. 1 <= temperatures.length <= 10의 5승
    -> O(n제곱)으로는 풀지 말아라 -> nlogn , n 의 시간복잡도를 가진 알고리즘으로 풀어야함.
    -> 완전 탐색으로 하게되면 n2 이므로 다른 방법 고안.
    -> sort()를 하게 되면 nlogn으로 시간 복잡도를 낮아질수 있지만 해당 문제에서는 정렬을 하면 안되므로 x
2. 30 <= temperatures[i] <= 100 -> 시간 복잡도에는 영향 x

예시 input output
intput : temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
output : [1, 1, 4, ,2, 1, 1, 0, 0]
"""
def dailyTemperatures(temperatures):
    # input arr 길이 만큼 answer 0 으로 초기화
    answer = [0] * len(temperatures)

    # 사용 할 stack 선언
    stack = []

    #enumerate는 반복문 사용 시 몇 번째 반복문인지 확인이 가능 -> 아래 형태와 같이 tuple 형태도 활용 가능하며 앞에 오는 것이 index 뒤가 value 이다.
    for current_day, current_temp in enumerate(temperatures):
        while stack and stack[-1][1] < current_temp:
            prev_day, _ = stack.pop()
            answer[prev_day] = current_day - prev_day
        #처음엔 비어 있으니 temperatures 값을 넣음
        stack.append((current_day, current_temp))
    return answer

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print(dailyTemperatures(temperatures))






