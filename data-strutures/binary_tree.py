
# https://medium.com/javarevisited/the-ultimate-guide-to-binary-trees-47112269e6fc


# There are two ways check both

#udacity course way


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print( tree.search(4))
# Should be False
print( tree.search(6))

# Test print(_tree
# Should be 1-2-4-5-3
print( tree.print_tree())




############## Grokking teh coding interview method #######################

from collections import deque

class TreeNode():
    def __init__(self,val):
        self.val =val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None: 
        return result
    
    queue = deque()
    queue.append(root)
    while queue:
        levelSize= len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()

            #add the node to teh current level
            currentLevel.append(currentNode.val)
            #insert children of current node in queue
            if currentNode.left :
                queue.append(currentNode.left)
            if currentNode.right :
                queue.append(currentNode.right)

        result.append(currentLevel)

    return result


# Time complexity #
# The time complexity of the above algorithm is O(N)O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

# Space complexity #
# The space complexity of the above algorithm will be O(N)O(N) as we need to return a list containing the level order traversal. We will also need O(N)O(N) space for the queue. Since we can have a maximum of N/2N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N)O(N) space to store them in the queue.

if __name__ == "__main__":
    root = TreeNode(12)
    root.left =   TreeNode(7)
    root.right = TreeNode(8)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(11)
    print("Level order traversal of binary tree is :\n", str(traverse(root)))    