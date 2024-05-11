
class Solution(object):
    def leafSimilar(self, root1, root2):
        def leaf(node, leaf_values):
            if not node:
                return leaf_values

            if node.left or node.right:
                leaf(node.left, leaf_values)
                leaf(node.right, leaf_values)
            else:
                leaf_values.append(node.val)

            return leaf_values

        leaf_values1 = leaf(root1, [])
        leaf_values2 = leaf(root2, [])

        # Print the lists for debugging
        print("List 1:", leaf_values1)
        print("List 2:", leaf_values2)

        return leaf_values1 == leaf_values2
        