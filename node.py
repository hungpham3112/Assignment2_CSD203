class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None
        self.next: Node | None = None
        self.prev: Node | None = None
