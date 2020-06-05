from Node import Node
class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def set_root(self,data):
        node = Node(data)
        if not self.root:
            self.root = node
        else:
            raise Exception('Root is not empty')
    def get_root(self):
        return self.root

    def insert_left(self,refer_node,data):
        node = Node(data)
        refnode = self.find(self.root,refer_node)
        if not  refnode.left:
            refnode.left = node
        else:
            raise Exception('Given node left is not empty')

    def insert_right(self,refer_node,data):
        node = Node(data)
        refnode = self.find(self.root,refer_node)
        if not refnode.right:
            refnode.right = node
        else:
            raise Exception('Given refer node right side is not empty')

    def find(self,ref_node,data):
        current = ref_node
        if current:
            if current.data == data:
                return current
            if current.left:
                temp1 = self.find(current.left,data)
                if temp1:
                    return temp1
            if current.right:
                temp2 = self.find(current.right,data)
                if temp2:
                    return temp2
        return None

    def height(self,ref_node):
        if not ref_node:
            return 0
        return max(self.height(ref_node.left),self.height(ref_node.right))+1

    def size(self,ref_node):
        if not ref_node:
            return 0
        return self.size(ref_node.left)+self.size(ref_node.right)+1

    def preOrderTraversal(self,ref_node):
        if not ref_node:
            return
        print(ref_node.data)
        self.preOrderTraversal(ref_node.left)
        self.preOrderTraversal(ref_node.right)
        
    def inOrderTraversal(self,ref_node):
        if not ref_node:
            return 0
        self.inOrderTraversal(ref_node.left)
        print(ref_node.data)
        self.inOrderTraversal(ref_node.right)

    def postOrderTraversal(self,ref_node):
        if not ref_node:
            return 0
        self.postOrderTraversal(ref_node.left)
        self.postOrderTraversal(ref_node.right)
        print(ref_node.data)

    def levelTraversal(self,ref_node):
        if not ref_node:
            return 0
        queue = []
        queue.append(ref_node)
        while queue:
            node = queue[0]
            del queue[0]
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
