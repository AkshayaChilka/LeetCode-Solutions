class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # Always push into stack_in
        self.stack_in.append(x)

    def pop(self) -> int:
        # Ensure stack_out has elements
        self.move()
        return self.stack_out.pop()

    def peek(self) -> int:
        # Ensure stack_out has elements
        self.move()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def move(self):
        # Transfer only when stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()