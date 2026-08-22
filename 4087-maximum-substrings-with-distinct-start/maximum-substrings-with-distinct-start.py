class Solution:
    def maxDistinct(self, s: str) -> int:
        seen = ""
        for i in s:
            if i in seen:
                continue
            else:
                seen = seen + i
        return len(seen)
            
        