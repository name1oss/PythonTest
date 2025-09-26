import numpy as np
import matplotlib.pyplot as plt

# 为了在图中正确显示中文和负号，建议添加以下两行设置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是一个常用的中文字体
plt.rcParams['axes.unicode_minus'] = False  # 修正负号'-'显示为方块的问题

# --- 1. 生成数据 ---
# 创建一个 x 轴的数据点数组，范围从 -3 到 3，共包含 100 个点
x = np.linspace(-3, 3, 100)

# 计算第一条曲线的 y 值：y = x^2
y1 = x**2

# 计算第二条曲线的 y 值：y = x^3
y2 = x**3

# --- 2. 创建画布并绘图 ---
# 创建一个图形画布，可以指定大小
plt.figure(figsize=(10, 6))

# 绘制第一条曲线 (y=x^2)
# color='blue' 设置颜色为蓝色
# linestyle='-' 设置为实线
# label='y = x²' 为曲线添加标签，用于图例显示
plt.plot(x, y1, color='blue', linestyle='-', label='$y = x^2$')

# 绘制第二条曲线 (y=x^3)
# color='red' 设置颜色为红色
# linestyle='--' 设置为虚线
# label='y = x³' 为曲线添加标签
plt.plot(x, y2, color='red', linestyle='--', label='$y = x^3$')


# --- 3. 美化图形 ---
# 添加图表标题
plt.title('二次函数与三次函数曲线图')

# 添加 x 轴和 y 轴的标签
plt.xlabel('X 轴')
plt.ylabel('Y 轴')

# 添加网格线，增加可读性
plt.grid(True)

# 显示图例 (自动根据 plot 函数中的 label 生成)
plt.legend()

# 在 x=0 和 y=0 处画出参考线
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)


# --- 4. 显示图形 ---
plt.show()