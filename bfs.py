from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes_at_level(root, target_level):
    if not root:
        return 0

    queue = deque([(root, 0)])  # Queue for BFS, along with the level of each node
    count = 0

    while queue:
        node, level = queue.popleft()

        if level == target_level:
            count += 1

        if level > target_level:
            break

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

    return count


# Create the binary tree
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#             \
#              7

# Define the nodes
node7 = TreeNode(7)
node6 = TreeNode(6, None, node7)
node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3, None, node6)
node2 = TreeNode(2, node4, node5)
root = TreeNode(1, node2, node3)

# Call the function to count nodes at level 2
target_level = 2
node_count = count_nodes_at_level(root, target_level)

# Print the result
print("Number of nodes at level", target_level, "is:", node_count)
