class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.head = None
        self.last = 0

    def insert(self, value):
        node = Node(value)
        if  self.head is None:
            self.head = node

        else:
            new = self.head
            while True:
                if value > new.value:
                    if new.right is None:
                        new.right = Node(value)
                        return
                    else:
                        new = new.right
                elif value < new.value:
                    if new.left is None:
                        new.left = Node(value)
                        return
                    else:
                        new = new.left

    def fromArray(self, array):
        for value in array:
           self.insert(value)

    def search(self, value):
        self.visited = 1
        new = self.head
        while ((new.left is not None) and (value < new.value)) or ((new.right is not None) and (value > new.value)):
            self.visited = self.visited + 1
            if new.value < value:
                new = new.right
            else:
                new = new.left

        if new.value is not value:
            return False
        else:
            return True


    def min(self):
        self.visited = 1
        new = self.head
        while new.left is not None:
            self.visited = self.visited + 1
            new = new.left

        return new.value

    def max(self):
        self.visited = 1
        new = self.head
        while new.right is not None:
            self.visited = self.visited + 1
            new = new.right

        return new.value

    def visitedNodes(self):
        return self.visited