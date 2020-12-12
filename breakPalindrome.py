"""
corner cases:
"aaaaa"
"aaaaaa"
"""
class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return ''
      
        s = list(s)
        for i in range(len(s)//2):
            if s[i] != 'a':
                s[i] = 'a'
                return ''.join(s)

        s[-1] = 'b'
        return ''.join(s)
