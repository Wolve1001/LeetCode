class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first = 0
        second = 0
        emp = []
        median = 0
        while first < len(nums1) and second < len(nums2): #add elements smaller first to the new list, by considering and comparing elements from both lists
            if nums1[first] < nums2[second]:
                emp.append(nums1[first])
                first+=1
            else:
                emp.append(nums2[second])
                second+=1
        while first < len(nums1): #add remaining elements from both lists
            emp.append(nums1[first])
            first += 1
        while second < len(nums2):
            emp.append(nums2[second])
            second += 1
        if len(emp) % 2 == 0: #find the median, since median is different for even length and odd length lists
            median = (emp[(len(emp) // 2) - 1] + emp[len(emp) // 2]) / 2
        else:
            median = emp[len(emp) // 2]
        
        return median
