class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if not self.rear:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None

        data = self.front.data
        self.front = self.front.next

        if not self.front:
            self.rear = None

        return data

    def is_empty(self):
        return self.front is None

    def print_list(self):

        current = self.front

        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("THE END")


def main():
    queue = Linked()
    queue.enqueue(12)
    queue.enqueue(31)
    queue.print_list()


main()
