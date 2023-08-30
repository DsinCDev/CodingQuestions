class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms = {}
        hmt = {}
        for i in range(len(s)):
            hms[s[i]] = hms.get(s[i],0) + 1
        for j in range(len(t)):
            hmt[t[j]] = hmt.get(t[j],0) + 1
        return hms == hmt

sol = Solution()
assert sol.isAnagram("dog","god") == True
assert sol.isAnagram("cat","sat") == False
assert sol.isAnagram("aaaaaa","aaaa") == False
assert sol.isAnagram("zzzzz","zzzzz") == True
assert sol.isAnagram("y","y") == True
assert sol.isAnagram("y","z") == False
