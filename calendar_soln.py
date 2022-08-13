class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        # if new node starts after current Node interval
        if node.start >= self.end:
            if not self.right:  # no node after current Node. We can add new node (Booking)
                self.right = node
                return True
            return self.right.insert(node)  # recursion

        # if new node starts before current Node interval
        elif node.end <= self.start:
            if not self.left:  # no node before current Node. We can add new node (Booking)
                self.left = node
                return True
            return self.left.insert(node)  # recursion'
        # This means the new node is overlapping with current Node
        else:
            return False


class Calendar:
    def __init__(self):
        self.root = None  # No booking

    def book(self, start: int, end: int) -> bool:
        if not self.root:  # first booking
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))  # check for booking


calendar = Calendar()
print(calendar.book(5, 10))
print(calendar.book(8, 13))
print(calendar.book(10, 15))
