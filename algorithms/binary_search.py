""" 
조건: 정렬된 array

먼저 array를 정렬한 후에
2분할을 한 지점의 값이 target과 같으면 인덱스를 반환
                  target보다 크면 왼쪽 array로 변경(인덱스도 같이)
                  target보다 작으면 오른쪽 array로 변경(인덱스도 같이)

그리고 다시 2분할 하여 반복한다.

종료는 더 이상 나눌 수 없는 경우(즉 원소가 하나 남은 경우)
"""

def solution(target, numbers):
    # 정렬
    numbers = sorted(numbers, reverse=False)

    start_idx, end_idx = 0, len(numbers)-1
    while start_idx <= end_idx:
        # 계속 바뀌는 sub array의 가운데 점을 찾기 위해서 + 
        mid = (start_idx + end_idx) // 2
        if numbers[mid] == target:
            return True
        elif numbers[mid] < target:
            start_idx = mid+1  # 오른쪽 array 선택
        else:
            end_idx = mid-1 # 왼쪽 array 선택

    return False

target = 8
numbers = [6, 3, 7, 2, 8, 1]
print(f"target {target} is in {solution(target, numbers)} for {numbers}")
