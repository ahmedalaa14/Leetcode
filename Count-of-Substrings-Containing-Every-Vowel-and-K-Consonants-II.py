class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set('aeiou')
        vowel_count, cons_count = defaultdict(int), 0 
        left = count = substrs = 0 
        def minus_char(char): 
            if char in vowels:
                vowel_count[char] -= 1
                if vowel_count[char] == 0:
                    del vowel_count[char] 
            else:
                nonlocal cons_count
                cons_count -= 1

        for char in word:
            if char in vowels:
                vowel_count[char] += 1
            else:
                cons_count += 1
                count = 0 

            while cons_count > k: 
                minus_char(word[left])
                left += 1

          
            while cons_count == k and len(vowel_count) == 5:
                count += 1 
                minus_char(word[left]) 
                left += 1 
            
          
            substrs += count

        return substrs