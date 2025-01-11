class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        bitmask = 0
        for char in s:
            bitmask ^= (1 << (ord(char) - ord('a')))

        odd_count = bin(bitmask).count('1')
        return odd_count <= k