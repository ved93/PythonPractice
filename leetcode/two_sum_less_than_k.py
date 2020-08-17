



def twoSumLessThanK(self, A: List[int], K: int) -> int:
    S = -1
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]+A[j] < K:
                S= max(S,A[i]+A[j])
    return S


# 2 pointers method
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        l,r = 0,len(A)-1
        A = sorted(A)
        S =-1
        while l < r:
            if A[l]+A[r] < K:
                S= max(S,A[l]+A[r] )
                l=l+1
            else :
                r = r-1
        return S    
    

# Complexity Analysis

# Time Complexity:  O(nlogn) to sort the array. The two pointers approach itself is  O(n), so the time complexity would be linear if the input is sorted.

# Space Complexity: from  O(logn) to  O(n), depending on the implementation of the sorting algorithm.

