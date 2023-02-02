class Node:
    def __init__(self, data):
        self.data = data
        self.right_branch = None
        self.left_branch = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node: Node):
        if data < node.data:
            if node.left_branch is None:
                node.left_branch = Node(data)
            else:
                self._insert(data, node.left_branch)
        else:
            if node.right_branch is None:
                node.right_branch = Node(data)
            else:
                self._insert(data, node.right_branch)

    def show(self):
        if self.root is not None:
            self._show(self.root)
        else:
            print("Tree is empty")

    def _show(self, node: Node):
        if node is not None:
            self._show(node.left_branch)
            self._show(node.right_branch)
            print(node.data)

    def struct_show(self):
        self._struct_show(self.root, 0, True)

    def _struct_show(self, node: Node, depth, is_root):
        if node is None:
            return
        if is_root:
            print(node.data)
        else:
            for i in range(depth):
                print("| ", end = "")
            print("\b\b--", node.data)
        self._struct_show(node.left_branch, depth + 1, False)
        self._struct_show(node.right_branch, depth + 1, False)

tree = Tree()
tree.insert(5)
tree.insert(13)
tree.insert(50)
tree.insert(12)
tree.insert(31)
tree.insert(22)
tree.insert(15)
tree.struct_show()
