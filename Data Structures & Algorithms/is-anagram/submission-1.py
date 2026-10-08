class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        # Use array to record the net frequency of each char
        counter=[0]*26
        for i in range(len(s)):
            counter[ord(s[i])-ord("a")]+=1
            counter[ord(t[i])-ord("a")]-=1
        
        # Iterate the array to check if there are non-zero net frequency for chars
        for e in counter:
            if e!=0:
                return False
        
        return True


# Time Complexity --> O(N)
# Space Complexity --> O(1)
