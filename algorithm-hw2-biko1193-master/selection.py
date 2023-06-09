import random

# 이 함수는 0-번째 원소를 피봇으로 정하고 그 왼편에는 더 작은 값들을 오른편에는 더 큰 값들이
# 오도록 원소의 위치를 변경한다. 반환값은 원소들의 위치가 바뀐 후 피봇의 인덱스이다.
def partition(list):
    pivot = list[0]
    L = 1 #좌측 시작 인덱스
    R = len(list) - 1 #우측 시작 인덱스
    while L <= R:
        while L <= R and list[L] < pivot:
            L += 1
        while L <= R and list[R] >= pivot:
            R -= 1
        if L <= R:
            list[L], list[R] = list[R], list[L]
    list[0], list[R] = list[R], list[0]
    return R

# 리스트 list에서 k번째로 작은 원소를 찾는다. 여기서 k >= 1이다.
# list의 한 원소를 랜덤으로 선택하고 이를 0번째 원소와 바꾼 후 partition()을 호출한다.
# partition() 함수를 호출하여 pivot의 위치를 반환하고 그 위치를 기준으로 왼편은 피봇보다 작은 값을,
# 오른편은 피봇보다 큰 값이 오도록 한다.
def selection(list, k):
    if len(list) == 1:
        return list[0]
    else:
        pivot_index = random.randint(0, len(list) - 1)
        list[0], list[pivot_index] = list[pivot_index], list[0]
        pivot_index = partition(list)
        if k == pivot_index + 1:
            return list[pivot_index]
        elif k < pivot_index + 1:
            return selection(list[:pivot_index], k)
        else:
            return selection(list[pivot_index + 1:], k - (pivot_index + 1))

list1 = [1, 2, 3, 4]
list2 = [2, 1, 4, 3]

list3 = [1,3,5,2,7,8,9,0,4,6]
list4 = [random.randint(1, 100) for _ in range(100)] #길이가 100인 랜덤 리스트 생성

print("selection함수 결과 : ", selection(list1, 2))  # 2 출력 예상
print("partition함수 결과 : ", partition(list2))  # 1 출력 예상
print()
print("리스트 :", list3, "\n결과 : ", selection(list3, 3))  # 2 출력 예상
print()
print("리스트 :", list4, "\n결과 : ", selection(list4, 10))


