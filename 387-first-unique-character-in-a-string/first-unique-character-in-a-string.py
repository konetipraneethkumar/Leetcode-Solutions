class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = {}
        for i,ch in enumerate(s):
            index[ch] = index.get(ch,0) + 1
        for i in range(len(s)):
            if index[s[i]] ==1:
                return i
        return -1


                  