
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    """
    Finds LCS of nodes p and q in the tree rooted at root.
    Note: p and q are TreeNode objects, not values.
    """
    
    # 1. Base Case
    if not root:
        return None
    
    # If we find either p or q, return the root itself
    if root == p or root == q:
        return root
    
    # 2. Recursive Search
    left_res = lowest_common_ancestor(root.left, p, q)
    right_res = lowest_common_ancestor(root.right, p, q)
    
    # 3. Decision Logic
    
    # If we found targets in BOTH subtrees, current node is the LCA
    if left_res and right_res:
        return root
    
    # Otherwise, return the non-None child (if any)
    # This bubbles up the found node (or the LCA found deeper)
    return left_res if left_res else right_res

# ---------------------------------------------------
# Driver Code
# ---------------------------------------------------
def build_sample_tree():
    #      3
    #     / \
    #    5   1
    #   / \ / \
    #  6  2 0  8
    #    / \
    #   7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    # Storing reference to nodes to pass as p and q
    nodes = {
        3: root,
        5: root.left,
        1: root.right,
        6: root.left.left,
        2: root.left.right,
        0: root.right.left,
        8: root.right.right,
        7: root.left.right.left,
        4: root.left.right.right
    }
    return root, nodes

if __name__ == "__main__":
    root, nodes = build_sample_tree()
    
    test_cases = [
        (nodes[5], nodes[1], 3),    # LCA of 5 and 1 is 3
        (nodes[5], nodes[4], 5),    # LCA of 5 and 4 is 5
        (nodes[6], nodes[4], 5),    # LCA of 6 and 4 is 5
        (nodes[0], nodes[8], 1),    # LCA of 0 and 8 is 1
        (nodes[6], nodes[2], 5)     # LCS of 6 and 2 is 5
    ]
    
    print(f"{'p':<5} | {'q':<5} | {'Expected':<10} | {'Result':<10} | {'Status'}")
    print("-" * 50)
    
    for p, q, expected_val in test_cases:
        res = lowest_common_ancestor(root, p, q)
        res_val = res.val if res else None
        status = "PASSED" if res_val == expected_val else "FAILED"
        print(f"{p.val:<5} | {q.val:<5} | {str(expected_val):<10} | {str(res_val):<10} | {status}")
