class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
    def pop(self) -> None:
        del self.stack[-1]
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return min(self.stack)

# Driver code
def main():
    obj = MinStack()
    obj.push(5)
    obj.push(2)
    obj.push(4)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(obj, param_3, param_4)
    obj.pop()
    print(obj.top())

# Run driver code if this file is not being imported
if __name__ == '__main__':
    main()