from node import Node


class NodeQ:
    def __init__(self, data):
        self.data = data
        self.next = None


class Myqueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def DeQueue(self):
        if self.isEmpty():
            return
        value = self.head.data
        self.head = self.head.next
        return value

    def EnQueue(self, data):
        node = NodeQ(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


class ProductBSTree:
    def __init__(self):
        self.root: Node | None = None

    def findFather(self, p):
        if self.root == None:
            return None
        if self.root.data == p:
            return None
        cur = self.root
        father = None
        while cur != None:
            if cur.data.Price == p:
                return father
            father = cur
            if cur.data.Price < p:
                cur = cur.right
            else:
                cur = cur.left
        return None

    def isEmpty(self):
        return self.root == None

    def insert(self, data):
        node = Node(data)
        if self.isEmpty():
            self.root = node
            return
        cur = self.root
        father = None
        pcode_data = int(data._pcode[1:])

        while cur != None:
            pcode_cur = int(cur.data._pcode[1:])
            if pcode_cur == pcode_data:
                return
            father = cur
            if pcode_cur < pcode_data:
                cur = cur.right
            else:
                cur = cur.left

        if int(father.data._pcode[1:]) < int(data._pcode[1:]):
            father.right = node
        else:
            father.left = node

    # function
    def insert2(self,node):
        if self.isEmpty():
            self.root = node
        else:
            curNode = self.root
            while curNode:
                if int(node.data._pcode[1:]) < int(curNode.data._pcode[1:]):
                    if curNode.left == None:
                        curNode.left = node
                    curNode = curNode.left
                elif int(node.data._pcode[1:]) > int(curNode.data._pcode[1:]):
                    if curNode.right == None:
                        curNode.right = node
                    curNode = curNode.right
                elif int(node.data._pcode[1:]) == int(curNode.data._pcode[1:]):
                    return f"{node.data._pcode} has existed"
        
    def findNode(self, pcode):  # tim node co key = p
        cur = self.root
        while cur != None:
            if cur.data._pcode == pcode:
                return cur.data
            else:
                if cur.data._pcode < pcode:
                    cur = cur.right
                else:
                    cur = cur.left
        return None  # can not find the node has key = p

    def visit(self, p):
        if p == None:
            return
        else:
            print(f"{p.data}", end=" ")

    def preOrder(self, p):
        if p == None:
            return
        else:
            self.visit(p)
            self.preOrder(p.left)
            self.preOrder(p.right)

    def postOrder(self, p):
        if p == None:
            return
        else:
            self.postOrder(p.left)
            self.postOrder(p.right)
            self.visit(p)

    def inOrder(self, p):
        if p == None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)

    def size(self):
        count = -1
        if self.root is not None:
            if self.root.left is not None:
                count += BST_size(root.left)
            if self.root.right is not None:
                count += BST_size(root.right)
        return count

    def breadth_first(self):
        queue = Myqueue()
        if self.root == None:
            return
        queue = Myqueue()
        queue.EnQueue(self.root)
        while not queue.isEmpty():
            p = queue.DeQueue()
            self.visit(p)
            if p.left != None:
                queue.EnQueue(p.left)
            if p.right != None:
                queue.EnQueue(p.right)

    def deleteNode(root, key):

        if root is None:
            return root

        if key < root.key:
            root.left = deleteNode(root.left, key)

        elif key > root.key:
            root.right = deleteNode(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = minValueNode(root.right)
            root.key = temp.key

            root.right = deleteNode(root.right, temp.key)

        return root

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def deleteByCopyLeft(self, p):
        q = self.findNode(p)
        if q == None or q.left == None:
            return
        cur = q.left
        father = None
        while cur.right != None:
            father = cur
            cur = cur.right
        # cur = node ngoai cung ben phai cua nhanh ben trai
        q.data = cur.data
        if q.left.right == None:
            q.left = q.left.left
        else:
            father.right = cur.left

    def deleteLeft(self, data):
        q = self.findNode(data)
        if q == None:
            return
        father = self.findFather(data)
        if father == None:
            if q.right == None:
                self.root = q.left
            else:
                self.root = q.right
            return

        if q.right == q.left == None:
            if father.data < q.data:
                father.right = None
            else:
                father.left = None
            return
        if q.right == None and q.left != None:
            father.right = q.left
            return
        if q.left == None and q.right != None:
            father.right = q.right
            return
        self.deleteByCopyLeft(data)

    def deleteByCopy(self, p):
        q = self.findNode(p)
        b = self.findFather(p)
        if self.root.data == p:
            self.root = None
            return
        if q == None:
            print(f"{p} k ton tai trong cay")
            return
        if q.right == None and q.left == None:
            if b.data > q.data:
                b.left = None
            if b.data < q.data:
                b.right = None
        if q.left == None and q.right != None:
            self.deleteByCopyRight(p)
        if q.left != None and q.right == None:
            self.deleteByCopyLeft(p)
        else:
            self.deleteByCopyLeft(p)

    def deleteByCopyRight(self, p):
        q = self.findNode(p)
        if q == None or q.right == None:
            return
        cur = q.right
        father = None
        while cur.left != None:
            father = cur
            cur = cur.left
        q.data = cur.data
        if q.right.left == None:
            q.right = q.right.right
        else:
            father.left = cur.right

    def deleteByMergingLeft(self, key):
        node = self.findNode(key)
        if node == None or node.left == None:
            return
        father = self.findFather(key)
        cur = node.left
        while cur.right != None:
            cur = cur.right
        cur.right = node.right
        if father == None:
            self.root = self.root.left
        else:
            if father.left.data == key:
                father.left = node.left
            else:
                father.right = node.left

    def deleteByMergingRight(self, key):
        node = self.findNode(key)
        if node == None or node.right == None:
            return
        father = self.findFather(key)
        cur = node.right
        while cur.left != None:
            cur = cur.left
        cur.left = node.left
        if father == None:
            self.root = self.root.right
        else:
            if father.right.data == key:
                father.right = node.right
            else:
                father.left = node.right

    def deleteByMerging(self, key):
        q = self.findNode(key)
        if q == None:
            return
        father = self.findFather(key)
        if father == None:
            if q.right == None:
                self.root = q.left
            else:
                self.root = q.right
            return
        if q.left == None:
            father.right = q
            return
        if q.right == None:
            father.left = q
            return
        self.deleteByMergingLeft(key)

    def rightRotate(self, data):
        p = self.findNode(data)
        father = self.findFather(data)
        if self.isEmpty() or p.left == None:
            return
        c = p.left
        temp = c.right
        c.right = p
        p.left = temp
        if father == None:
            self.root = c
            return
        if father.data < data:
            father.right = c
        else:
            father.left = c
        return

    # display

    def invisit(self):
        self.inOrder(self.root)
        return

    def postvisit(self):
        self.postOrder(self.root)

    def previsit(self):
        self.preOrder(self.root)

    def turnLeft(self, nodeList): 
        if self.isEmpty():
            print("Nothing in the list")
            return
        nodeList = nodeList[::-1]
        i = 0
        for node in nodeList:
            node.left = None
            node.right = None
        for node in nodeList:
            if i == 0:
                self.root = node
            else:
                self.insert2(node)
            i += 1

    def balanceTree(self):
        self.turnLeft(self.inorderNode(self.root))
        self.convertAVLtree(self.root)

    def convertAVLtree(self, root):
        nodes = []
        self.storeBSTNodes(root, nodes)
        n = len(nodes)
        self.root = self.buildTree(nodes, 0, n-1)

    nodeList = []
    def inorderNode(self, curNode):
        if self.isEmpty():   
            return None        
        if curNode == None:
            return
        else:
            self.inorderNode(curNode.left)
            self.nodeList.append(curNode)
            self.inorderNode(curNode.right)
            return self.nodeList
    def storeBSTNodes(self, root, nodes):
        if not root:
            return
        self.storeBSTNodes(root.left, nodes)
        nodes.append(root)
        self.storeBSTNodes(root.right, nodes)

    def buildTree(self, nodes, start, end):
        if start > end:
            return None
        mid = (start+end) // 2
        node = nodes[mid]
    
        node.left = self.buildTree(nodes, start, mid-1)
        node.right = self.buildTree(nodes, mid+1, end)
        return node
