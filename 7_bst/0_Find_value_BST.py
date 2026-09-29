"""
Problem: Find Value Binary Search Tree
Category: Binary Search Trees
Pattern: Binary Search Tree Property (Left < Root < Right)

Time Complexity:  O(H) - O(log N) average, O(N) worst-case skewed tree
Space Complexity: O(1) iterative / O(H) recursive stack
"""


class BST:
    # Function to search a node in BST.
    def search(self, node, x):
        # code here
        # if node is None:
        #     return 0
        # if node.data == x: return 1
        # elif node.data < x:
        #     return self.search(node.right,x)
        # return self.search(node.left,x)

        if node is None:
            return 0
        q = [node]
        while q:
            curr = q.pop(0)
            if curr is not None:
                if curr.data == x:
                    return 1
                elif curr.data < x:
                    q.append(curr.right)
                else:
                    q.append(curr.left)
        return 0
