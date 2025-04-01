import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 生成模拟数据
np.random.seed(42)
data = pd.DataFrame({
    'X_value': np.random.rand(50) * 100,  # X轴数值 (0-100)
    'Y_value': np.random.rand(50) * 100,  # Y轴数值 (0-100)
    'Size': np.random.randint(10, 1000, 50),  # 气泡大小 (10-1000)
    'Category': np.random.choice(['A', 'B', 'C'], 50)  # 分组颜色
})

# 创建颜色映射字典
color_map = {
    'A': '#FF6B6B',  # 红色系
    'B': '#4ECDC4',  # 青色系
    'C': '#45B7D1'  # 蓝色系
}

# 创建画布和坐标轴
plt.figure(figsize=(12, 8), dpi=100)

# 绘制气泡图
scatter =plt.scatter(
    x=data['X_value'],
    y=data['Y_value'],
    s=data['Size'],
    color=data['Category'].map(color_map),  # 修改此处
    alpha=0.7,
    edgecolors='black',
    linewidth=0.5
)

# 添加图例（自定义图例显示大小）
legend_sizes = [100, 500, 1000]
legend_labels = [f'Size: {size}' for size in legend_sizes]
for size in legend_sizes:
    plt.scatter([], [],  # 空数据
                s=size,
                c='gray',
                alpha=0.7,
                edgecolors='black',
                label=str(size))

# 设置图表元素
plt.title('Bubble Chart Example', fontsize=16, pad=20)
plt.xlabel('X Axis Label', fontsize=12)
plt.ylabel('Y Axis Label', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)  # 添加网格线

# 添加颜色分类图例
category_legend = plt.legend(
    handles=scatter.legend_elements()[0],
    title="Categories",
    loc='upper right',
    bbox_to_anchor=(1.25, 1)
)

# 添加尺寸图例
size_legend = plt.legend(
    title="Bubble Sizes",
    loc='upper right',
    bbox_to_anchor=(1.25, 0.7)
)

# 将两个图例都添加到图表
plt.gca().add_artist(category_legend)

# 调整布局防止文字被截断
plt.tight_layout()

# 显示图表
plt.show()

# 保存图表（可选）
# plt.savefig('bubble_chart.png', bbox_inches='tight')