'''
First non repeating character in the string
1) abcdabc
ans: d

2) aaabbbcddd
ans: c

Solution:
1) Brute force:
Use two pointers: 
for each character, there will be one more loop checking each character again. 

for i in range(len(s)):
    for j in range(len(s)):
        if i != j and s[i] == s[j]
            break
    
    return s[i]
    

2) Use hash map
time complexity: O(n)
space complexity: O(n)
'''

def firstNonRepeatingChar(s):
    hash = {}
    for char in s:
        if char in hash:
            hash[char] += 1
        else:
            hash[char] = 1
            
    for char in s:
        if hash[char] == 1:
            return char
    
    return "_"    

print(firstNonRepeatingChar("abcdabc"))
print(firstNonRepeatingChar("aaabbbcddd"))
print(firstNonRepeatingChar("abcabc"))
