# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity

- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code

```
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m != 0:
            cut_point = m if m > 1 else 1
            nums1_parsed = nums1[0:cut_point]
        else:
            nums1_parsed = []
        
        if n != 0:
            cut_point = n if n > 1 else 1
            nums2_parsed = nums2[0:cut_point]
        else:
            nums2_parsed = []
        
        new_list = nums1_parsed + nums2_parsed
        new_list.sort()

        for idx, n in enumerate(new_list):
          nums1[idx] = n
```
