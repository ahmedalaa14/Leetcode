class Solution(object):
    def spiralMatrix(self, m, n, head):
        moves = [[0,1], [1,0], [0,-1], [-1,0]]
        res = [[-1 for _ in range(n)] for _ in range(m)]

        top, btm, left, right = 1, m-1, 0, n-1 
        move = 0
        r, c = 0, 0
        curr = head
        while curr is not None:
            res[r][c] = curr.val

            if move % 4 == 0 and c == right:
                right -= 1
                move += 1
            elif move % 4 == 2 and c == left:
                left += 1
                move += 1
            elif move % 4 == 3 and r == top:
                top += 1
                move += 1
            elif move % 4 == 1 and r == btm:
                btm -= 1
                move += 1
            
            r += moves[move % 4][0]
            c += moves[move % 4][1]

            curr = curr.next
        
        return res