class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build the freqency map
        freq_mp = Counter(nums)

        # use a list of buckets to store the number frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in freq_mp.items():
            buckets[val].append(key)

        # reverse iterate the buckets list to find the k freqent element
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
