# 리스트의 모든 원소 더하기
def test(list):
    if not list:
        return 0
    return list.pop(0) + test(list)

list = [1, 2, 3, 4, 5]
result = test(list)
print(result)

# 리스트의 원소 순서대로 출력
def test2(list2):
    if not list:
        return 0
    print(list.pop(0))
    test2(list)

list2 = [1, 2, 3, 4, 5]
result2 = test2(list2)
print(result2)

# 리스트의 원소 역순 출력
