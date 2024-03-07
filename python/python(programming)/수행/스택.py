# 스텍 ADT 지우지 말고 저장해놓기
stack_size=5
list=[None]*stack_size
top=-1
def isEmpty():
    if top==-1:
        return 1
    else:
        return 0

def isFull():
    if top==stack_size-1:
        return 1
    else:
        return 0

def push(i):
    global top
    if not isFull():
        top+=1
        list[top]=i
        print(list)
        return
    else:
        print('스텍가득참')
        return
    
def pop():
    global top
    if not isEmpty():
        item=list[top]
        top-=1
        print(item)
        return
    else:
        print('스텍 비어있음')
        return

def peek():
    if not isEmpty():
        print(list[top])
        return
    else:
        print("스텍 빔")
        return

push(1)
pop()
push(2)
push(3)
peek()