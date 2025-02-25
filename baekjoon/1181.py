n=int(input())
list=[]
for i in range(n):
    a=input()
    list.append(a)
list=set(list)
list=sorted(list,key=lambda x:(len(x),x))
for i in list:
    print(i)