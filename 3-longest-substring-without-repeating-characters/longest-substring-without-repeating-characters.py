class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}      # Store the last index of each character
        left = 0             # Start of the current window
        max_length = 0       # Longest length found so far

        for right, char in enumerate(s):

            # If character was seen inside the current window
            if char in seen and seen[char] >= left:

                # Move left after the previous occurrence
                left = seen[char] + 1

            # Update the character's latest index
            seen[char] = right

            # Calculate current window length
            max_length = max(max_length, right - left + 1)

        return max_length