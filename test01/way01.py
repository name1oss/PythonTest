from typing import List

class Solution:
    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        """
        方法一：排序法
        """
        # 对数组进行降序排序
        nums.sort(reverse=True)
        # 返回第 k 大的元素，其索引为 k-1
        return nums[k-1]

# 示例
solver = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"方法一，数组 {nums} 中第 {k} 大的元素是: {solver.findKthLargest_sort(nums, k)}") # 输出 5

nums_2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k_2 = 4
print(f"方法一，数组 {nums_2} 中第 {k_2} 大的元素是: {solver.findKthLargest_sort(nums_2, k_2)}") # 输出 4