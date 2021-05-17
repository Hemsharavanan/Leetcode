class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        asciiValues = [0] * 26
        
        for char in s:
            index = ord(char) - 97
            asciiValues[index] += 1
            
        for char in t:
            index = ord(char) - 97
            asciiValues[index] -= 1
            
        for value in asciiValues:
            if value != 0:
                return False
        return True

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""