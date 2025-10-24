from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        使用回溯法（深度优先搜索）解决子集问题
        """
        result = []  # 存放所有子集
        path = []    # 存放当前正在构建的子集

        def backtrack(start_index: int):
            """
            :param start_index: 本轮选择的起始索引
            """
            
            # 1. 收集子集：将当前路径的“快照”（拷贝）存入结果
            #    使用 path[:] 来创建一个 path 列表的浅拷贝
            result.append(path[:])

            # 2. 检查终止条件（可选，但隐含在 for 循环中）
            #    如果 start_index 已经到达数组末尾，for 循环将不会执行
            if start_index == len(nums):
                return

            # 3. 遍历选择列表
            #    从 start_index 开始，到数组末尾
            for i in range(start_index, len(nums)):
                
                # 4. 做出选择
                current_num = nums[i]
                path.append(current_num)
                
                # 5. 进入下一层决策
                #    注意：传入 i + 1，表示下一轮只能选择 i 后面的元素
                backtrack(i + 1)
                
                # 6. 撤销选择（回溯）
                #    将 path 恢复到进入本层循环之前的状态
                path.pop()

        # 从索引 0 开始启动回溯
        backtrack(0)
        return result

# --- 示例运行 ---
if __name__ == "__main__":
    solver = Solution()
    
    nums1 = [1, 2, 3]
    print(f"输入: {nums1}")
    # 输出: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]] (顺序可能不同)
    print(f"输出: {solver.subsets(nums1)}")

    nums2 = [0]
    print(f"\n输入: {nums2}")
    # 输出: [[], [0]]
    print(f"输出: {solver.subsets(nums2)}")