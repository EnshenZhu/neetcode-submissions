class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize the result, prefix and suffix arrays
        N = len(nums)
        res = [0] * N
        prefix_arr = [0] * N
        suffix_arr = [0] * N

        # the first element of the prefix and the last element of the suffix need to be 1
        prefix_arr[0] = suffix_arr[N - 1] = 1

        # handle the prefix array
        for i in range(1, N):
            prefix_arr[i] = prefix_arr[i - 1] * nums[i - 1]

        # handle the suffix array
        for i in range(N - 2, -1, -1):
            suffix_arr[i] = suffix_arr[i + 1] * nums[i + 1]

        # get the result by prefix_arr * suffix_arr
        for i in range(N):
            res[i] = prefix_arr[i] * suffix_arr[i]

        return res
