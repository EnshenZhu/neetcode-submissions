from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_cluster = defaultdict(list)
        for word in strs:
            letter_arr = (
                [0] * 26
            )  # letter_arr will be the unique key (after convert to tuple) for the word_cluster
            for char in word:
                letter_arr[ord(char) - ord("a")] += 1  # producing the unique key
            word_cluster[tuple(letter_arr)].append(word)

        return list(word_cluster.values())
