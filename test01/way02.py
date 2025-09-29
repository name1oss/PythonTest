import heapq
from typing import List

class Solution:
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        """
        方法二：最小堆法
        """
        # 初始化一个空列表作为最小堆
        min_heap = []
        
        # 遍历数组中的所有元素
        for num in nums:
            # 将当前元素推入堆中
            heapq.heappush(min_heap, num)
            
            # 如果堆的大小超过 k，就弹出堆顶（最小的）元素
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # 遍历结束后，堆顶元素即为第 k 大的元素
        return min_heap[0]

# 示例
solver = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"方法二，数组 {nums} 中第 {k} 大的元素是: {solver.findKthLargest_heap(nums, k)}") # 输出 5

nums_2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k_2 = 4
print(f"方法二，数组 {nums_2} 中第 {k_2} 大的元素是: {solver.findKthLargest_heap(nums_2, k_2)}") # 输出 4