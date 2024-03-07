    # 스텍 ADT 지우지 말고 저장해놓기
class stack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.list=[None]*stack_size
        self.top=-1

    def isEmpty(self):
        if top==-1:
            return 1
        else:
            return 0

    def isFull(self):
        if top==self.stack_size-1:
            return 1
        else:
            return 0

    def push(self):
        global top
        if not self.isFull():
            top+=1
            list[top]=i
            print(list)
            return
        else:
            print('스텍가득참')
            return
        
    def pop(self):
        global top
        if not self.isEmpty():
            item=list[top]
            top-=1
            print(item)
            return
        else:
            print('스텍 비어있음')
            return

    def peek(self):
        if not self.isEmpty():
            print(list[top])
            return
        else:
            print("스텍 빔")
            return
        
    def index(self): # 나만의 ADT
        for i in range(self.top + 1):
            print("인덱스번호:{}".format(self.stack[i]))

    def remove_all(self): # 나만의 ADT
        self.list=[None]*self.stack_size
        top=-1
        print("스택 내의 모든 요소 제거!")
        return
    
    def remove(self, item): # 나만의 ADT
        if item in self.list:
            self.list.remove(item)
            top -= 1
            print(f"{item}이(가) 스택에서 삭제")


    push(1)
    pop()
    push(2)
    push(3)
    peek()