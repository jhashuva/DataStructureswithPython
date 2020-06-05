from Node import Node
class BinarySeaarchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        node = Node(data)
        if not self.root:
            self.root = node
        else:
            current = self.root
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left
                    if not current:
                        parent.left = node
                        return
                else:
                    current = current.right
                    if not current:
                        parent.right = node
                        return


    def search(self,data):
        current = self.root
        while True:
            if not current:
                return None
            elif current.data == data:
                return data
            elif current.data> data:
                current = current.left
            else:
                current = current.right

    def get_node_with_parent(self,data):
        parent = None
        current = self.root
        if not current:
            return(None, None)
        while True:
            if current.data == data:
                return (None,current)
            elif current.data>data:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

        return (parent, current)

    def remove(self,data):
        parent,node = self.get_node_with_parent(data)

        if not node and not parent:
            return None
        children_count = 0
        if node.left and node.right:
            children_count = 2
        elif not node.left and not node.right:
            childern_count = 0
        else:
            children_count = 1

        if children_count == 0:
            if parent:
                if parent.right is node:
                    parent.right = None
                else:
                    parent.left = None
            else:
                self.root = None
        elif children_count == 1:
            next_node = None
            if node.left:
                next_node = node.left
            else:
                next_node = node.right

            if parent:
                if parent.left is node:
                    parent.left = next_node
                else:
                    parent.right = next_node
            else:
                self.root = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right
            while leftmost_node.left:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left

            node.data = leftmost_node.data

            if parent_of_leftmost_node == leftmost_node:
                parent_of_leftmost_node.left = leftmost_node.right
            else:
                parent_of_leftmost_node.right = leftmost_node.right



    def pre_order(self,current):
        if not current:
            return 0
        #current = self.root
        print(current.data)
        self.pre_order(current.left)
        self.pre_order(current.right)


    def in_order(self,current):
        if not current:
            return 0
        #current = self.root

        self.in_order(current.left)
        print(current.data, end=' ')
        self.in_order(current.right)


    def post_order(self,current):
        if not current:
            return 0
        #current = self.root
        self.post_order(current.left)
        self.post_order(current.right)
        print(current.data)

    def levelOrderTraversal(self,current):
        if not current:
            return 0
        #current = self.root
        queue = []
        queue.append(current)
        while queue:
            node=queue[0]
            del queue[0]
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
