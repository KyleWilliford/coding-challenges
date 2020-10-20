"""
Create by Jiehan Zhu at 10/19/2020

Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Constraints:
Methods pop, top and getMin operations will always be called on non-empty stacks.
"""


class MinStack:
    """
    Runtime: 772 ms. Your runtime beats 15.50 % of python3 submissions.
    Memory Usage: 17.8 MB
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


class MinStack2:
    """
    Runtime: 60 ms. Your runtime beats 79.70 % of python3 submissions.
    Memory Usage: 17.8 MB
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        elif self.min[-1] > x:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        del self.stack[-1]
        del self.min[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# test case
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3
minStack.pop()
assert minStack.top() == 0
assert minStack.getMin() == -2

minStack = MinStack2()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3
minStack.pop()
assert minStack.top() == 0
assert minStack.getMin() == -2