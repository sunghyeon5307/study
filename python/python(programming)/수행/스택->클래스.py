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

    push(1)
    pop()
    push(2)
    push(3)
    peek()