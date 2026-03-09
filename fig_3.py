import numpy as np
import matplotlib.pyplot as plt

# 定义条件概率密度函数
def f_X_given_Y(x, y=2):
    """
    条件概率密度函数 f_{X|Y}(x|2)
    """
    result = np.zeros_like(x)
    mask = (x >= -2) & (x <= 2)
    result[mask] = (x[mask] + 2) / 8
    # 其他情况下 result 已经是 0
    return result

# 创建 x 值数组，覆盖整个定义域
x = np.linspace(-3.5, 3.5, 1000)

# 计算对应的 y 值
y_values = f_X_given_Y(x)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(x, y_values, label=r'$f_{X|Y}(x|2) = \frac{x+2}{8}$ for $-2 \leq x \leq 2$', color='blue', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8)  # x轴
plt.axvline(0, color='black', linewidth=0.8)  # y轴

# 设置图形属性
plt.title(r'Conditional Probability Density Function $f_{X|Y}(x|2)$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel(r'$f_{X|Y}(x|2)$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# 标记关键点
plt.plot([-2, 2], [0, 0.5], 'ro', markersize=6, label='Key Points')  # 关键点 (-2,0) 和 (2,0.5)
plt.annotate('(-2, 0)', xy=(-2, 0), xytext=(-2.5, 0.1),
             arrowprops=dict(arrowstyle='->', color='red'))
plt.annotate('(2, 0.5)', xy=(2, 0.5), xytext=(2.2, 0.55),
             arrowprops=dict(arrowstyle='->', color='red'))

# 设置坐标轴范围
plt.xlim(-3.5, 3.5)
plt.ylim(-0.05, 0.7)

# 显示图形
plt.tight_layout()
plt.savefig('fig_3.png', dpi=450, bbox_inches='tight')
plt.show()

# 打印函数定义
print("函数定义:")
print(r"f_{X|Y}(x|2) = (x+2)/8  当 -2 <= x <= 2")
print("              = 0         其他情况")

# 验证一些特定点
test_points = [-2.5, -2, 0, 1, 2, 2.5]
print("\n验证特定点:")
for pt in test_points:
    val = f_X_given_Y(np.array([pt]))[0]
    print(f"x = {pt}: f(x|2) = {val}")

