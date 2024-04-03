### 매소드 ###


# format() : 문자열에 변수를 삽입 or 형식을 지정하는데 사용
print('Hello, {}. I am {} years old'.format('ds', 50))
# Hello, ds. I am 50 years old


# count() : 특정 문자나 문자열이 등장하는 횟수를 세는 데 사용
print('Hello, python'.count('o'))
# 2


# find() : 특정 문자나 문자열이 처음 등장하는 인덱스를 반환
# 찾고자 하는 문자나 문자열이 없는 경우 -1을 반환
print('Hello, python'.find('o'))
# 4
print('Hello, python'.find('w'))
# -1


# index() : 특정 문자나 문자열이 처음 등장하는 인덱스를 반환
print('Hello, python'.index('o'))
# 4


# 대소문자 변환
print('hihi, hahaha'.upper()) # 소문자 -> 대문자
print('HIHI, HAHAHA'.lower()) # 대문자 -> 소문자
print('hihi, hahaha'.capitalize()) # 첫 글자만 대문자, 나머지 소문자
print('hihi, hahaha'.title()) # 단어의 첫 글자 대문자, 나머지 소문자
# HIHI, HAHAHA
# hihi, hahaha
# Hihi, hahaha
# Hihi, Hahaha


# join() : 문자열 리스트를 하나로 합쳐 하나의 문자열로 변환
print(', '.join(['apple', 'banana', 'orange']))
# apple, banana, orange


# split() : 문자열을 특정 문자를 기준으로 분리하여 리스트를 생성
print('apple, banana, orange'.split(', '))
# ['apple', 'banana', 'orange']


# extend
animals = ['cat', 'dog']
more = ['tiger', 'lion']
animals.extend(more)
print(animals)
# ['cat', 'dog', 'tiger', 'lion']


# insert
animals = ['dog', 'cat']
animals.insert(1, 'elephant')
print(animals)
# ['dog', 'elephant', 'cat']


# clear
animals = ['cat', 'dog']
print(animals.clear())
# None


# pop
animals = ['cat', 'dog', 'tiger']
removed = animals.pop(1)
print(removed)
print(animals)
# ['cat', 'tiger']


# remove
animals = ['cat', 'dog', 'tiger', 'dog']
animals.remove('dog')
print(animals)
# ['cat', 'tiger', 'dog']


# 교집합(intersection())
f1 = {'ha', 'stop'}
f2 = {'ha', 'oh', 'stop'}
result1 = f1.intersection(f2)
print(result1)


# 합집합(union())
result2 = f1.union(f2)
print(result2)


# 차집합(defference())
result_diff = fruits1.difference(fruits2)
print(result_diff)



print("----------------------")
haha = ['apple', 'banana', 'apple', 'cherry', 'apple']
print(haha.count("apple"))

print(haha.index("banana"))

print("apple banana apple cherry apple".title())

num = [1,2,3,4]
more = [5]
num.extend(more)
print(num)

list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)

fruits = ['apple', 'orange', 'grape']
fruits.insert(2, 'banana')
print(fruits)

numbers = [1,2,3,4,5]
numbers.remove(5)
print(numbers)
print("----------------------")
