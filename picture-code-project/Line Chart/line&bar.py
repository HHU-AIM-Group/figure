import matplotlib.pyplot as plt
import numpy as np

# 数据
type_labels_cub = ["Qwen-VL", "Meta Learning", "Meta Learning w/ LA"]
mismathch_cub = [2242, 855, 785]
qwen_right_cub = [328, 699, 715]
has_right_cub = [2037, 837, 776]
re_right_cub = [1079, 740, 727]
accuracy_cub = [45.00, 93.60, 96.40]
re_accuracy_cub = [59.92, 94.54, 96.64]

type_labels_cifar = ["Qwen-VL", "Meta Learning", "Meta Learning w/ LA"]
mismathc_cifar = [2824, 539, 535]
qwen_right_cifar = [142, 426, 411]
has_right_cifar = [2603, 512, 505]
re_right_cifar = [1922, 427, 430]
accuracy_cifar = [37.04, 95.18, 94.64]
re_accuracy_cifar = [68.22, 95.20, 95.02]

# 定义条形图的位置
bar_width = 0.3
index = np.arange(len(type_labels_cub))

# 创建图表
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.4))

# 绘制左侧CUB的堆叠条形图
ax1.bar(index - bar_width/2, mismathch_cub, bar_width, label='Mismatch Case', color='#A6ECF5')
ax1.bar(index + bar_width/2, has_right_cub, bar_width, label='Gold in Mismatch', color='#87CEFA')
# ax1.bar(index - bar_width/2, qwen_right_cub, bar_width, label='Initial Right Case', color='#56b0e8')
# ax1.bar(index + bar_width/2, re_right_cub, bar_width, label='Final Match Case', color='#FFA500')

# 创建第二个 y 轴
ax1_twin = ax1.twinx()
ax1_twin.plot(index, accuracy_cub, marker='o', linestyle='-', color='#e377c2', label='Initial Inference')
ax1_twin.plot(index, re_accuracy_cub, marker='s', linestyle='--', color='#9467bd', label='Final Inference')
ax1_twin.set_ylabel('Accuracy (%)', fontsize=14)
ax1_twin.legend(loc='center right')

# 设置左侧CUB的图表标题和标签
ax1.set_title('CUB', fontsize=14)
ax1.set_ylabel('Count', fontsize=14)
ax1.set_xticks(index)
ax1.set_xticklabels(type_labels_cub, fontsize=14, rotation=10)
ax1.legend(loc="center right", bbox_to_anchor=(1, 0.7))
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# 设置 y 轴上的刻度标签字体大小
ax1.yaxis.set_tick_params(labelsize=12)
ax1_twin.yaxis.set_tick_params(labelsize=12)

# 绘制右侧CIFAR的堆叠条形图
ax2.bar(index - bar_width/2, mismathc_cifar, bar_width, label='Mismatch Case', color='#A6ECF5')
ax2.bar(index + bar_width/2, has_right_cifar, bar_width, label='Gold in Mismatch', color='#87CEFA')
# ax2.bar(index - bar_width/2, qwen_right_cifar, bar_width,  label='Contain Right Answer', color='#56b0e8')
# ax2.bar(index + bar_width/2, re_right_cifar, bar_width, label='Contain Right Answer', color='#FFA500')

# 创建第二个 y 轴
ax2_twin = ax2.twinx()
ax2_twin.plot(index, accuracy_cifar, marker='o', linestyle='-', color='#e377c2', label='Initial Inference')
ax2_twin.plot(index, re_accuracy_cifar, marker='s', linestyle='--', color='#9467bd', label='Final Inference')
ax2_twin.set_ylabel('Accuracy (%)', fontsize=14)
ax2_twin.legend(loc='center right')

# 设置右侧CIFAR的图表标题和标签
ax2.set_title('CIFAR', fontsize=14)
ax2.set_ylabel('Count', fontsize=14)
ax2.set_xticks(index)
ax2.set_xticklabels(type_labels_cifar, fontsize=14, rotation=10)
ax2.legend(loc="center right", bbox_to_anchor=(1, 0.7))
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# 设置 y 轴上的刻度标签字体大小
ax2.yaxis.set_tick_params(labelsize=12)
ax2_twin.yaxis.set_tick_params(labelsize=12)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()
# plt.savefig('filter3_2.pdf', bbox_inches='tight')
