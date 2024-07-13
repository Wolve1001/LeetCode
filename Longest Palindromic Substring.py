class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: #edge case, if string is empty
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)     # Odd length palindromes
            len2 = self.expandAroundCenter(s, i, i + 1) # Even length palindromes
            max_len = max(len1, len2) #return max length only
            if max_len > (end - start): #value of start and end need to be changed as per the results
                start = i - (max_len - 1) // 2
                end = i + max_len // 2 

        return s[start:end + 1] #use slicing to give final answer
    
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]: 
          #start the loop from the given point/points, for odd length since there will be a mid element s[left] will be equal to s[right] on first pass, but for even length palindrome check first if the two elements are the same
            left -= 1 #expand, one pointer towards left one toowards right
            right += 1
        return right - left - 1 #returns the length of the palindrome
