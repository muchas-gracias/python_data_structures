

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    #  traverses the left most node down, then up to the parent, then to the
    #  right most node in the sub tree, then up
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def print_inorder(self):
        print("In-order traversal:", self.inorder_traversal())

    #  traverses the root node, then goes down the left side of the sub-tree
    #  then right
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)

        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def print_preorder(self):
        print("Pre-order traversal:", self.preorder_traversal())

    #  traverse all the way down the left sub tree then grabs the left, then
    #  right and up
    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)

    def print_postorder(self):
        print("Post-order traversal:", self.postorder_traversal())


def main():
    bst = BST()

    bst.insert("Greg")
    bst.insert("Walker")
    bst.insert("James")

    bst.print_preorder()


main()
