"""
* in-place

인덱스 0에서 시작하여,
기준점을 오른쪽으로 하나씩 변경해가며,
각 기준점에서 왼쪽 원소들과의 비교를 통해 왼쪽으로 옮길지 말지를 판단한다.

따라서 본인보다 큰 원소가 왼쪽에 나타나는 경우에는 break 할 수 있기 때문에,
"주어진 데이터에 정렬성이 어느정도 존재할 때" 효율적이다.
"""

def solution(numbers):
    for i in range(len(numbers)):
        # 역순으로 비교 i -> i-1 -> .. -> 1
        for j in range(i, 0, -1):
            if numbers[j-1] > numbers[j]:
                # swap
                temp = numbers[j]
                numbers[j] = numbers[j-1]
                numbers[j-1] = temp
    return numbers

numbers = [6, 3, 7, 2, 8, 1]
print(f"{numbers} -> {solution(numbers)}")