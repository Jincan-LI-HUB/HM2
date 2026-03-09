import numpy as np
import matplotlib.pyplot as plt

# 定义条件期望函数
def conditional_expectation(y):
    """
    条件期望 E[X|Y=y] = y/3
    """
    return y / 3

# 创建 y 值数组，范围 [0, 6]
y = np.linspace(0, 6, 400)

# 计算对应的 E[X|Y=y] 值
expec_x = conditional_expectation(y)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(y, expec_x, label=r'$\mathbb{E}[X|Y = y] = \frac{1}{3}y$', color='green', linewidth=2)

# 标记端点
plt.plot([0, 6], [0, 2], 'go', markersize=8, label='Endpoints')

# 添加注释
plt.annotate('$(0, 0)$', xy=(0, 0), xytext=(0.5, 0.2),
             arrowprops=dict(arrowstyle='->', color='red', lw=1),
             fontsize=12, color='red')
plt.annotate('$(6, 2)$', xy=(6, 2), xytext=(5, 2.3),
             arrowprops=dict(arrowstyle='->', color='red', lw=1),
             fontsize=12, color='red')

# 设置图形属性
plt.title(r'Conditional Expectation $\mathbb{E}[X|Y = y] = \frac{1}{3}y$, $y \in [0, 6]$', fontsize=14)
plt.xlabel(r'$y$', fontsize=12)
plt.ylabel(r'$\mathbb{E}[X|Y = y]$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# 设置坐标轴范围
plt.xlim(-0.2, 6.2)
plt.ylim(-0.2, 2.2)

# 添加y=x/3这条直线的参考网格线
for i in range(1, 7):
    plt.axhline(i/3, color='lightgray', linestyle=':', alpha=0.5)
for i in range(1, 6):
    plt.axvline(i, color='lightgray', linestyle=':', alpha=0.5)

# 显示图形
plt.tight_layout()
plt.savefig('fig_4.png', dpi=450, bbox_inches='tight')
plt.show()

# 打印公式
print("条件期望公式:")
print("E[X|Y = y] = y/3, 其中 y ∈ [0, 6]")

# 验证几个特定点
print("\n验证特定点:")
test_ys = [0, 1.5, 3, 4.5, 6]
for y_val in test_ys:
    exp_val = conditional_expectation(y_val)
    print(f"y = {y_val}: E[X|Y={y_val}] = {exp_val}")


