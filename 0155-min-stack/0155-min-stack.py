class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.len = 0
        

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if self.len:
            self.min_stack.append(min(val,self.min_stack[self.len -1]))
        else:
            self.min_stack.append(val)
        self.len += 1

    def pop(self) -> None:
        self.len -= 1
        self.min_stack.pop()
        return self.stack.pop()
        
    
        

    def top(self) -> int:
        return self.stack[self.len -1]
                              
        

    def getMin(self) -> int:
        return self.min_stack[self.len-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()