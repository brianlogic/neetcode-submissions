class MinStack:

    def __init__(self):
        self.stack = [] # keep a normal stack to support push pop top 
        self.prevMin = [] # prefix to track min element


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prevMin: 
            self.prevMin.append(min(val, self.prevMin[-1]))
        else: 
            self.prevMin.append(val)

    def pop(self) -> None:
        self.prevMin.pop() 
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prevMin[-1]
