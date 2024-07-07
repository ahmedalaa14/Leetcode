class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        str1 = ""
        str2 = ""
        for i in word1 :
            str1 = str1 + i 
        for j in word2 :
            str2 = str2 + j    
        if str1 == str2 :
            return True
        return False    