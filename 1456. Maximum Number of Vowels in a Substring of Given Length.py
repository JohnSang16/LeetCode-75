#Given a string s and an integer k, return the maximum number of vowel letters
#  in any substring of s with length k.

#Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        point1 = 0
        point2 = k 
        maxsum = 0
        strlst = list(s)
        for i in range(k):
            if self.isVowel(strlst[i]):
                maxsum += 1
        if maxsum == k:
            return k
        else:  
            while point1 < len(strlst)-k and point2 < len(strlst):
    
                if maxsum == k:
                    return k
                if self.isVowel(strlst[point2]) and self.isVowel(strlst[point1]):
                    pass
                elif self.isVowel(strlst[point2]) and self.isVowel(strlst[point1]) is not True:
                    maxsum += 1 
                elif self.isVowel(strlst[point2]) is not True and self.isVowel(strlst[point1]):
                    maxsum -= 1
                elif self.isVowel(strlst[point2]) is not True and self.isVowel(strlst[point1]) is not True:
                    pass
                point1 += 1
                point2 += 1 
                return k

    def isVowel(self, char):
        vowellst = 'aeiouAEIOU'
        if char in vowellst:
            return True
            
c = Solution()
maxVowel = c.maxVowels('leetcode', 3)
print(maxVowel)