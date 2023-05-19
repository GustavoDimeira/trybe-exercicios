from node import Node


class Queue:
    def __init__(self):
        self.head_value = None
        self.tail_value = None
        self.__length = 0

    def print_values(self):        
        crr_value = self.head_value
        for x in range(self.__length):
            print("Posição: ", x, "\nValor: ", crr_value.value, "\n\n")
            crr_value = crr_value.next

    def push(self, value):
        last_value = Node(value)
        old_last = self.tail_value

        if (old_last):
            old_last.next = last_value
            last_value.previous = old_last
            self.tail_value = last_value
        else:
            self.head_value = last_value
            self.tail_value = last_value

        self.__length += 1
        return last_value

    def pop(self):
        new_last = self.tail_value.previous
        old_last = self.tail_value

        new_last.next = None
        self.tail_value = new_last

        self.__length -= 1
        return old_last


queue = Queue()

queue.print_values()

queue.push("gustavo")
queue.push("dimeira")
queue.push(1)
queue.push(2)
queue.push(3)
queue.push({"a": 1, "b": 2, "c": "c"})
queue.push([1, 2, 3])

queue.print_values()
print("-----")
print(queue.pop())
print("-----")
print(queue.pop())
print("-----")
queue.print_values()