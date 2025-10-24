### 推演过程与思路

要找到一个集合的所有子集（幂集），我们有两种主流的思考路径：**回溯法（递归）** 和 **迭代法**。

#### 思路一：回溯法 (Backtracking)

回溯法是一种通过“深度优先搜索”(DFS) 来探索所有可能解的算法。我们可以将其想象成在遍历一棵“决策树”。

对于 `nums` 数组中的**每一个元素**，我们都有两种决策：

1.  **“要”**：将这个元素放入当前的子集中。
2.  **“不要”**：不将这个元素放入当前的子集中。


将问题看作：从 `nums` 中“选出 0 个元素”、“选出 1 个元素”、“选出 2 个元素”... 直到“选出 $n$ 个元素”的所有**组合**。

**算法流程：**

1.  定义一个递归函数 `backtrack(start_index, current_path)`：

      * `start_index`：表示我们*本轮*可以从 `nums[start_index]` 开始选择元素。
      * `current_path`：表示当前已经构建的子集路径。

2.  定义一个全局的 `result` 列表，用来存放所有子集。

3.  **递归步骤：**

      * **立刻收集：** 只要进入 `backtrack` 函数，就说明 `current_path` 是一个合法的子集（包括空集 `[]`）。我们立即将其（的拷贝）加入 `result`。
          * `result.append(current_path[:])`
      * **遍历选择：** 从 `start_index` 开始，向后遍历 `nums` 数组。
          * `for i in range(start_index, len(nums)):`
          * **a. 做出选择：** 将 `nums[i]` 添加到 `current_path` 中。
              * `current_path.append(nums[i])`
          * **b. 继续探索：** 递归调用 `backtrack`，开始下一轮的选择。
              * **关键：** 传入 `i + 1` 而不是 `start_index + 1`。这确保了下一轮选择只会从 `i` 之后的元素开始，避免了产生重复的组合（例如，如果有了 `[1, 2]`，就不会再产生 `[2, 1]`）。
              * `backtrack(i + 1, current_path)`
          * **c. 撤销选择（回溯）：** 当 (b) 中的递归调用返回时，说明以 `nums[i]` 开头的路径已经探索完毕。我们必须将 `nums[i]` 从 `current_path` 中移除，以便 `for` 循环可以继续尝试下一个元素（例如，尝试 `nums[i+1]`）。
              * `current_path.pop()`

4.  **启动：** 从 `backtrack(0, [])` 开始调用。

**模拟 `nums = [1, 2, 3]`：**

```
backtrack(0, [])
-> res.append([])
-> i=0 (选 1): path=[1]
   -> backtrack(1, [1])
      -> res.append([1])
      -> i=1 (选 2): path=[1, 2]
         -> backtrack(2, [1, 2])
            -> res.append([1, 2])
            -> i=2 (选 3): path=[1, 2, 3]
               -> backtrack(3, [1, 2, 3])
                  -> res.append([1, 2, 3])
                  -> (i=3, 循环结束)
               -> path.pop() -> path=[1, 2]
            -> (i=3, 循环结束)
         -> path.pop() -> path=[1]
      -> i=2 (选 3): path=[1, 3]
         -> backtrack(3, [1, 3])
            -> res.append([1, 3])
            -> (i=3, 循环结束)
         -> path.pop() -> path=[1]
      -> (i=3, 循环结束)
   -> path.pop() -> path=[]
-> i=1 (选 2): path=[2]
   -> backtrack(2, [2])
      -> res.append([2])
      -> i=2 (选 3): path=[2, 3]
         -> backtrack(3, [2, 3])
            -> res.append([2, 3])
            -> ...
         -> path.pop() -> path=[2]
   -> path.pop() -> path=[]
-> i=2 (选 3): path=[3]
   -> backtrack(3, [3])
      -> res.append([3])
      -> ...
   -> path.pop() -> path=[]
-> (i=3, 循环结束)
```
