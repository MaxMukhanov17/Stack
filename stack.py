class Stack():
    def __init__(self) -> None:
        self.stack = []

    def isEmpty(self):
        if not self.stack:
            return True
        else:
            return False


    def push(self, item):
        self.stack.append(item)


    def pop(self):
        if len(self.stack) == 0:
            return None
        remote = self.stack.pop()
        return remote

    def peek(self):
        last_element = self.stack[-1]
        return last_element

    def size(self):
        len_stack = len(self.stack)
        return len_stack

s = Stack()
print(s.stack)