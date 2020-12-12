class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return ''
      
        s = list(s)
        for index, char in enumerate(s):
            if char != 'a':
                if len(s)%2 and len(s)//2 == index:
                    break
                else:
                    s[index] = 'a'
                    return ''.join(s)

        s[-1] = 'b'
        return ''.join(s)
