""" 
* in-place (no extra memory)

인덱스 0부터 시작하여,
인덱스 0에 들어갈 가장 작은 숫자를 오른쪽으로 순차적으로 비교하며 swap 해준다.
다음 인덱스 1에 들어갈 가장 작은 숫자를 오른쪽으로 순차적으로 비교하며 swap 해준다.
...
"""

def solution(numbers):
    for i in range(len(numbers)):
        print(f'--- 인덱스 {i}에 들어갈 최소 숫자 찾기 ---')
        # i+1 -> 왼쪽은 가장 작은 숫자로 변경되었기 때문에,
        #        오른쪽만 탐색하면 된다.
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                # swap
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers

numbers = [6, 3, 7, 2, 8, 1]
print(f"{numbers} -> {solution(numbers)}")