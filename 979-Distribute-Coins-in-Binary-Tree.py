class Solution:
    def __init__(self):
        self.moves = 0

    def distributeCoins(self, root):
        self.postOrder(root)
        return self.moves

    def postOrder(self, root):
        if root is None:
            return 0

        leftExcess = self.postOrder(root.left)
        rightExcess = self.postOrder(root.right)

        self.moves += abs(leftExcess) + abs(rightExcess)

        return root.val + leftExcess + rightExcess - 1