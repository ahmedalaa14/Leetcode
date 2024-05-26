class Solution:
    def checkRecord(self, n):
        
        MOD = int(1e9+7)

        def matmul(A, B):
            C = [[0 for _ in range(6)] for _ in range(6)]
            for k in range(6):
                for i in range(6):
                    for j in range(6): C[i][j] = (C[i][j]+A[i][k]*B[k][j])%MOD
            return C
        
        def pow(A, n):
            if n==1: return A
            
            t = pow(A, int(n/2))
            t = matmul(t, t)

            if (n%2)==0: return t
            else: return matmul(A, t)
        
        t = pow([[1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]], n)
        
        return sum([t[i][0] for i in range(6)])%MOD
        