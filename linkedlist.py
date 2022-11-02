from node import Node


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def __repr__(self):
        current = self.head
        node = []
        while current:
            node.append(current.data)
            current = current.next
        return "".join(map(str, node))

    def isempty(self):
        return self.head is None and self.tail is None

    def append(self, node: Node):
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, node: Node):
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
            node.prev = None
        self.size += 1

    def insert_after_index(self, index: int, node: Node):
        index += 1
        if self.size == 0:
            raise IndexError
        elif index == 0:
            self.prepend(node)
        elif index == len(self) + 1:
            self.append(node)
        elif 0 < index < len(self) + 1:
            count = 0
            assert isinstance(self.head, Node)
            head = self.head
            while count < index - 2:
                assert isinstance(head, Node)
                head = head.next
                count += 1
            assert isinstance(head, Node)
            node.next = head.next
            head.next = node
            self.size += 1
        else:
            raise IndexError

    def sort_by_object(self):
        pass

    def pop_code(self, pcode: str):
        pass

    def search(self, code):
        pass

    def pop_after_code(self, code):
        pass


class ProductLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def search(self, code):
        current = self.head
        while current != None:
            if current.data._pcode == code:
                return current.data
            current = current.next
        return False

    def sort_by_object(self):
        i = 0
        n = len(self)
        while i < n:
            j = 0
            cur = self.head
            while j < n - i and cur.next:
                if int(cur.data._pcode[1:]) > int(cur.next.data._pcode[1:]):
                    cur.data, cur.next.data = cur.next.data, cur.data
                cur = cur.next
                j += 1
            i += 1

    def pop_after_code(self, pcode: str):
        if len(self) == 1 or self.head == None:
            return
        current = self.head
        while current.next:
            product = current.data
            if product._pcode == pcode:
                current.next = current.next.next
                self.size -= 1
                return product
            current = current.next

    def pop_code(self, pcode: str):
        if len(self) == 1 or self.head == None:
            return
        if self.head.data._pcode == pcode:
            temp = self.head
            self.head = self.head.next
            return temp
        current = self.head
        while current.next:
            product = current.next
            if product.data._pcode == pcode:
                current.next = current.next.next
                self.size -= 1
                return product
            current = current.next


class CustomerLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def search(self, code):
        current = self.head
        while current != None:
            if current.data._ccode == code:
                return current.data
            current = current.next
        return False

    def pop_code(self, ccode: str):
        if len(self) == 1 or self.head == None:
            return

        if self.head.data._ccode == ccode:
            temp = self.head
            self.head = self.head.next
            return temp

        current = self.head
        while current.next:
            customer = current.next
            if customer.data._ccode == ccode:
                current.next = current.next.next
                self.size -= 1
                return customer
            current = current.next


class OrderingLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def search_ccode(self, code):
        current = self.head
        while current != None:
            if current.data._ccode == code:
                return current.data
            current = current.next
        return False

    def search_pcode(self, code):
        current = self.head
        while current != None:
            if current.data._pcode == code:
                return current.data
            current = current.next
        return False

    def sort_by_object(self):
        i = 0
        n = len(self)
        while i < n:
            j = 0
            cur = self.head
            assert isinstance(cur, Node)
            while j < n - i and cur.next:
                if int(cur.data._pcode[1:]) > int(cur.next.data._pcode[1:]):
                    cur.data, cur.next.data = cur.next.data, cur.data
                elif int(cur.data._pcode[1:]) == int(cur.next.data._pcode[1:]):
                    if int(cur.data._ccode[1:]) > int(cur.next.data._ccode[1:]):
                        cur.data, cur.next.data = cur.next.data, cur.data
                cur = cur.next
                j += 1
            i += 1
