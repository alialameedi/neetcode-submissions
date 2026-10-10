class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # look at each string
        # sort it
        # put sorted string with sorted to value array of [original_word1, 2, 3, etc]
        # return array of the values

        anagrams = {}

        for i in strs:

            sorted_word = "".join(sorted(i))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(i)
            else:
                anagrams[sorted_word] = [i]

        return list(anagrams.values())

        