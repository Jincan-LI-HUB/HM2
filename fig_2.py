import numpy as np
import matplotlib.pyplot as plt

def f_X_given_A(x):
    """
    条件概率密度函数 f_{X|A}(x|A)
    """
    x = np.asarray(x)
    result = np.zeros_like(x, dtype=float)
    mask = (x >= 1) & (x <= 2)
    result[mask] = (3/7) * (x[mask]**2)
    return result

# 创建 x 值数组，覆盖整个定义域
x = np.linspace(0, 3, 1000)

# 计算对应的 f_{X|A}(x|A) 值
pdf_values = f_X_given_A(x)

# 计算最大值用于设置 y 轴范围
max_value = (3/7) * (2**2)  # x=2 时取得最大值
print(f"函数在 x=2 处的最大值: {max_value:.4f}")

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(x, pdf_values, label=r'$f_{X|A}(x|A) = \frac{3}{7}x^2$ for $x \in [1,2]$', color='purple', linewidth=2)

# 填充 [1,2] 区间内的区域
x_fill = np.linspace(1, 2, 500)
y_fill = f_X_given_A(x_fill)
plt.fill_between(x_fill, y_fill, alpha=0.3, color='purple', label='PDF support')

# 标记区间 [1,2] 的边界
plt.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Support boundary')
plt.axvline(x=2, color='red', linestyle='--', alpha=0.7)

# 标记关键点
plt.plot([1, 2], [f_X_given_A(1), f_X_given_A(2)], 'ro', markersize=6, label='Boundary values')

# 在关键点添加注释
plt.annotate(f'({1}, {f_X_given_A(1):.3f})', xy=(1, f_X_given_A(1)), 
             xytext=(1.2, f_X_given_A(1)+0.05), fontsize=10,
             arrowprops=dict(arrowstyle='->', color='red'))
plt.annotate(f'({2}, {f_X_given_A(2):.3f})', xy=(2, f_X_given_A(2)), 
             xytext=(2.1, f_X_given_A(2)-0.15), fontsize=10,
             arrowprops=dict(arrowstyle='->', color='red'))

# 设置图形属性
plt.title(r'Conditional PDF $f_{X|A}(x|A) = \frac{3}{7}x^2$, $x \in [1,2]$', fontsize=14)
plt.xlabel('$x$', fontsize=12)
plt.ylabel(r'$f_{X|A}(x|A)$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10)

# 设置坐标轴范围
plt.xlim(0, 3)
plt.ylim(0, max_value*1.1)

# 显示图形
plt.tight_layout()
plt.savefig('fig_2.png', dpi=450, bbox_inches='tight')
plt.show()

# 打印函数定义
print("函数定义:")
print(r"f_{X|A}(x|A) = (3/7)x^2  当 x ∈ [1,2]")
print("              = 0          其他情况")

# 验证几个特定点
print("\n验证特定点:")
test_points = [0, 0.5, 1, 1.5, 2, 2.5, 3]
for pt in test_points:
    val = f_X_given_A(pt)
    print(f"x = {pt}: f(x|A) = {val:.4f}")

# 验证积分是否等于1（归一化性质）
from scipy.integrate import quad
result, error = quad(lambda x: (3/7)*x**2, 1, 2)
print(f"\n积分验证 ∫₁² (3/7)x² dx = {result:.6f} (误差: {error:.2e})")
print(f"理论值应为1: {'✓ 正确' if abs(result-1)<1e-10 else '✗ 错误'}")

# 理论计算积分验证
theoretical_result = (3/7) * (2**3 - 1**3) / 3
print(f"理论计算: (3/7) × (8-1)/3 = (3/7) × 7/3 = {theoretical_result:.6f}")


