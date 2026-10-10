class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for i in strs:

            sorted_word = "".join(sorted(i))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(i)
            else:
                anagrams[sorted_word] = [i]

        return list(anagrams.values())

        