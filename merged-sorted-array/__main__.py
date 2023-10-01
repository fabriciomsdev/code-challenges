from dataclasses import dataclass
from typing import Dict, List


@dataclass
class TestContext:
    input: Dict
    expected: List


scenarios = [
    TestContext(
        input={
            'nums1': [1,2,3,0,0,0],
            'm': 3,
            'nums2': [3,4,5],
            'n': 3,
        },
        expected=[1,2,3,3,4,5]
    )
]


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

        return nums1

for scenario in scenarios:
    result = Solution().merge(**scenario.input)
    assert result == scenario.expected