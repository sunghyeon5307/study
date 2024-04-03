    # 스텍 ADT 지우지 말고 저장해놓기
class Stack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.list=[None]*stack_size
        self.top=-1

    def isEmpty(self):
        if self.top==-1:
            return 1
        else:
            return 0

    def isFull(self):
        if self.top==self.stack_size-1:
            return 1
        else:
            return 0

    def push(self,i):
        #global self.top
        if not self.isFull():
            self.top+=1
            self.list[self.top]=i
            #print(list)
        else:
            print('스텍가득참')
            return
        
    def pop(self):
        #global top
        if not self.isEmpty():
            self.top-=1
            #print(item)
            return self.list[self.top+1]
        else:
            print('스텍 비어있음')
            return

    def peek(self):
        if not self.isEmpty():
            return self.list[self.top]
        else:
            print("스텍 빔")
            return

def precedence(op):
    if op == '(' or op == ')' : return 0
    elif op == '+' or op == '-' : return 1
    elif op == '*' or '/' : return 2
    else: return - 1

def Infix2Postfix(expr):
    s = Stack(100)
    output = []

    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif term in '+-/*':
            while not s.isEmpty():
                op = s.peek()
                if precedence(term) <= precedence(op):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:
            output.append(term)
        
    while not s.isEmpty():
            output.append(s.pop())
        
    return output
    
infix1 = input()
infix1 = list(infix1)
postfix1 = Infix2Postfix(infix1)
print(postfix1)
    