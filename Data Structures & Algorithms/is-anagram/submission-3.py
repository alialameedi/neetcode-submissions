class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        first_word = {}
        second_word = {}

        for i in s:
            if i in first_word:
                first_word[i] += 1
            else:
                first_word[i] = 1

        for j in t:
            if j in second_word:
                second_word[j] += 1
            else:
                second_word[j] = 1

        for key in first_word:
            if key not in second_word:
                return False
            elif first_word[key] != second_word[key]:
                return False

        for key in second_word:
            if key not in first_word:
                return False
            elif second_word[key] != first_word[key]:
                return False

        
        return True
        