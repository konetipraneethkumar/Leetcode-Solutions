class Solution:
    def maxDistinct(self, s: str) -> int:
        seen = ""
        for i in range(len(s)):
            if s[i] in seen:
                continue
            else:
                seen = seen + s[i]
        return len(seen)
            
        