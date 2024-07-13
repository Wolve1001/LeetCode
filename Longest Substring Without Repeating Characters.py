class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() #create a set to avoid duplicates
        l_list = 0
        right = 0
        left = 0
        while right < len(s):
            if s[right] not in char_set: 
                char_set.add(s[right]) #we use add for set, not append
                right += 1 
                l_list = max(l_list, right - left) #check for maximum length of substring
            else:
                char_set.remove(s[left]) #if element already in set, start removing the leftmost element from the set until set is empty again
                left += 1
        return l_list
