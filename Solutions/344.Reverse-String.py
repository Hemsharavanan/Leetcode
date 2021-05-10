class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

"""
Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""