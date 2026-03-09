import numpy as np
import matplotlib.pyplot as plt

# 定义概率密度函数的各段
def f_X_part1(x):
    """第一段: -2 <= x < 0"""
    return -x / 4

def f_X_part2(x):
    """第二段: 0 <= x <= 3"""
    c = 1/18
    return c * x**2

# 创建各段的x值
x_left = np.linspace(-3.2, -2, 100)     # x < -2 (函数值为0)
x1 = np.linspace(-2, 0, 500, endpoint=False)  # -2 <= x < 0
x2 = np.linspace(0, 3, 500)           # 0 <= x <= 3
x_right = np.linspace(3, 4.2, 100)      # x > 3 (函数值为0)

# 计算对应的y值
y_left = np.zeros_like(x_left)        # 零值区域
y1 = f_X_part1(x1)
y2 = f_X_part2(x2)
y_right = np.zeros_like(x_right)      # 零值区域

# 分别绘制各段
plt.figure(figsize=(12, 6))

# 绘制零值区域
plt.plot(x_left, y_left, 'k-', linewidth=2, alpha=0.7, label=r'$f_X(x) = 0$, $x < -2$')
plt.plot(x_right, y_right, 'k-', linewidth=2, alpha=0.7, label=r'$f_X(x) = 0$, $x > 3$')

# 绘制非零部分
plt.plot(x1, y1, 'b-', linewidth=2, label=r'$f_X(x) = -\frac{1}{4}x$, $-2 \leq x < 0$')
plt.plot(x2, y2, 'g-', linewidth=2, label=r'$f_X(x) = \frac{1}{18}x^2$, $0 \leq x \leq 3$')

# 添加分段点的标记
plt.plot(-2, f_X_part1(np.array([-2])), 'ro', markersize=6, fillstyle='full')  # 实心圆点
plt.plot(0, f_X_part1(np.array([0])), 'ro', markersize=6, fillstyle='none')    # 空心圆点 (左极限)
plt.plot(0, f_X_part2(np.array([0])), 'ro', markersize=6, fillstyle='full')    # 实心圆点 (右极限)
plt.plot(3, f_X_part2(np.array([3])), 'ro', markersize=6, fillstyle='full')    # 实心圆点

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# 设置坐标轴标签
plt.xlabel('x')
plt.ylabel(r'$f_X(x)$')
plt.title(r'Probability Density Function')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# 设置坐标轴范围
plt.xlim(-3.2, 4.2)
plt.ylim(-0.05, max(max(y1), max(y2))*1.1)

# 保存图像
plt.savefig('fig_1.png', dpi=450, bbox_inches='tight')
plt.show()

# 输出关键点值
c = 1/18
print(f"c = {c}")
print(f"f_X(-2) = {-(-2)/4} = 0.5 (included)")
print(f"f_X(0-) = {-0/4} = 0 (not included in first segment)")
print(f"f_X(0+) = {c*0**2} = 0 (included in second segment)")
print(f"f_X(3) = {c*3**2} = {c*9} = 0.5 (included)")
print(f"Function equals zero for x < -2 and x > 3")



