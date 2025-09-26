# **Python 算法实现与数据可视化实验报告**

### **摘要**

本报告记录了一次基于Python语言的编程实验。实验核心内容分为两部分：首先，针对“求解数组中第k大的元素”这一经典算法问题，设计并实现了两种不同的解决方案——排序法和最小堆法；其次，利用`numpy`和`matplotlib`库对算法的理论时间复杂度以及基本数学函数进行了数据可视化。报告详细记述了实验目的、环境、过程与结果，并对实验中遇到的`ModuleNotFoundError`问题及其解决方案进行了分析与总结。

-----

### **一、 实验目的**

1.  掌握使用Python解决具体算法问题的能力。
2.  学习并实现两种查找第k大元素的方法，并理解其底层逻辑。
3.  通过数据可视化，直观地分析和比较不同算法的时间复杂度。
4.  熟练掌握`numpy`库进行科学计算和`matplotlib`库进行数据绘图的基本操作。
5.  学习诊断和解决Python开发环境中常见的第三方库依赖问题。

-----

### **二、 实验环境**

* **操作系统**: Windows (根据截图推断)
* **编程语言**: Python 3.13 (根据截图路径推断)
* **主要库**:
    * `numpy`
    * `matplotlib`
* **开发工具**: PowerShell / VS Code

-----

### **三、 实验内容与过程**

#### **第一部分：求解第k大元素算法实现**

**1. 问题描述**

给定一个整数数组 `nums` 和一个整数 `k`，要求找出数组中第 `k` 个最大的元素。

**2. 方法一：排序法**

此方法思路直接，首先对整个数组进行降序排序，然后直接返回索引为 `k-1` 的元素即可。该方法的初始方案参考了图1。

**图1：初始解法参考**

* **代码实现**:
    ```python
    from typing import List

    def findKthLargest_sort(nums: List[int], k: int) -> int:
        """
        方法一：排序法
        """
        # 对数组进行降序排序
        nums.sort(reverse=True)
        # 返回第 k 大的元素，其索引为 k-1
        return nums[k-1]
    ```

**3. 方法二：最小堆法**

为了寻求更高效率的解法，引入了最小堆。该方法维护一个大小为 `k` 的最小堆，遍历数组，最终堆顶元素即为所求。

* **代码实现**:
    ```python
    import heapq
    from typing import List

    def findKthLargest_heap(nums: List[int], k: int) -> int:
        """
        方法二：最小堆法
        """
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
    ```

#### **第二部分：算法复杂度与函数曲线可视化**

**1. 算法复杂度对比**

为了直观比较上述两种方法的时间复杂度 (O(NlogN) vs O(Nlogk))，我们编写了脚本来绘制它们的理论操作数增长曲线。

* **代码实现**:
    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 生成数据
    N = np.arange(100, 10001, 100)
    time_sort = N * np.log2(N) # 排序法
    time_heap_k10 = N * np.log2(10) # 最小堆法 (k=10)
    time_heap_k_n_div_4 = N * np.log2(N / 4) # 最小堆法 (k=N/4)

    # 绘图
    plt.figure(figsize=(12, 8))
    plt.plot(N, time_sort, label='排序法: $O(N \log N)$')
    plt.plot(N, time_heap_k10, label='最小堆法: $O(N \log k)$ (当 k=10)', linestyle='--')
    plt.plot(N, time_heap_k_n_div_4, label='最小堆法: $O(N \log k)$ (当 k=N/4)', linestyle=':')
    plt.title('排序法 vs 最小堆法 时间复杂度对比')
    plt.xlabel('数组元素数量 (N)')
    plt.ylabel('理论操作次数')
    plt.legend()
    plt.grid(True)
    plt.show()
    ```
* **结果分析**:
    从图中可以明显看出，当`k`为较小的常数时，最小堆法的性能（接近线性）远优于排序法。随着`k`值的增大，其性能逐渐接近排序法。

**2. Matplotlib基础绘图练习**


* **代码实现**:
    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    x = np.linspace(-3, 3, 100)
    y1 = x**2
    y2 = x**3

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, color='blue', label='$y = x^2$')
    plt.plot(x, y2, color='red', linestyle='--', label='$y = x^3$')
    plt.title('二次函数与三次函数曲线图')
    plt.xlabel('X 轴')
    plt.ylabel('Y 轴')
    plt.grid(True)
    plt.legend()
    plt.show()
    ```
* **结果展示**:
<img width="1250" height="750" alt="Image" src="https://github.com/user-attachments/assets/337fad5e-d2ce-4afc-ba08-c47aa40f2a7d" />

-----

### **四、 实验中遇到的问题与解决方法**

* **问题描述**:
    在初次运行绘图脚本时，程序中断并抛出 `ModuleNotFoundError: No module named 'numpy'` 错误，如下图2所示。

    **图2：实验中遇到的错误**

* **原因分析**:
    该错误信息明确指出，执行代码的Python环境中缺少名为 `numpy` 的模块。这是因为 `numpy` 和 `matplotlib` 并非Python标准库，需要手动安装才能使用。

* **解决方法**:
    使用Python的包管理工具`pip`来安装所缺失的库。在PowerShell终端中执行以下命令：

    ```bash
    py -m pip install numpy matplotlib
    ```

    等待命令执行完毕，相关库被成功下载并安装到Python环境中。之后再次运行脚本，程序便能正常执行，并成功绘制出图形。

-----

### **五、 实验总结**

通过本次实验，我成功实现了两种查找数组第k大元素的算法，并深入理解了它们的工作原理和性能差异。排序法简单直观，但时间复杂度固定；最小堆法在 `k` 值远小于数组长度 `N` 的场景下具有显著的效率优势。

更重要的是，我熟练掌握了使用`numpy`和`matplotlib`进行数据处理和可视化的流程。通过绘制复杂度曲线，我能够将抽象的算法分析转化为直观的图形对比，加深了对理论知识的理解。

最后，解决`ModuleNotFoundError`的经历让我认识到，搭建稳定可靠的开发环境是编程实践的第一步，熟练使用`pip`等工具管理项目依赖至关重要。本次实验全面锻炼了我的算法设计、代码实现、数据分析和问题调试能力。
