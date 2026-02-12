
#1768. Merge Strings Alternately

#You are given two strings word1 and word2. Merge the strings by adding letters in 
# alternating order, starting with word1. If a string is longer than the other, 
# append the additional letters onto the end of the merged string. Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

import time
class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        #init empty str
        merged_string = ""  
         #n is to store the len of whichever str is longer 
        n = 0
        if(len(word1)>=len(word2)):
            n = len(word1)
        else:
             n = len(word2)
        for i in range(n): 
            #add str chars in alternating order
            if i < len(word1):
                merged_string += word1[i]
            if i < len(word2):
                merged_string += word2[i]
        return merged_string
            
c = Solution()
test1 = c.mergeAlternately("abc", "pqr")
test2 = c.mergeAlternately("ab", "pqrs")
test3 = c.mergeAlternately("abcd", "pq")
print("-------------------Test Cases:----------------")
print(f"test1 output:{test1}, expected output: apbqcr")
print(f"test2 output:{test2}, expected output: apbqrs")
print(f"test3 output:{test3}, expected output: apbqcd")
print("         runtime approx: 47ms, Solved: T")
