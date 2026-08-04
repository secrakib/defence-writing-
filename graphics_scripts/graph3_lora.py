import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('e:/Writing Defence/graphics', exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'legend.fontsize': 11,
    'figure.dpi': 300,
    'axes.axisbelow': True
})

categories = ['BanglaT5 (247M)', 'mBART-50 (611M)', 'NLLB-200 (615M)']
full_params = [247, 611, 615]
lora_params = [4.7, 9.8, 9.8] # Millions

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={'width_ratios': [1.5, 1]})

# Left Chart: Total vs Trainable Parameters
y = np.arange(len(categories))
height = 0.35

rects1 = ax1.barh(y - height/2, full_params, height, label='Total Parameters (Frozen)', color='#95a5a6', edgecolor='black')
rects2 = ax1.barh(y + height/2, lora_params, height, label='LoRA Trainable Parameters', color='#e74c3c', edgecolor='black')

ax1.set_xlabel('Parameter Count (Millions)')
ax1.set_yticks(y)
ax1.set_yticklabels(categories)
ax1.legend(loc='lower right')
ax1.set_title('Parameter Efficiency of LoRA Fine-Tuning')
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Add values on bars
for p in ax1.patches:
    width = p.get_width()
    ax1.annotate(f'{width:.1f}M',
                xy=(width, p.get_y() + p.get_height() / 2),
                xytext=(3, 0),
                textcoords="offset points",
                ha='left', va='center', fontsize=9)

# Right Chart: Parameter Reduction %
ax2.axis('off')
ax2.set_title('Trainable Parameter Reduction', pad=20)

for i, (full, lora) in enumerate(zip(full_params, lora_params)):
    reduction = (1 - (lora / full)) * 100
    circle = plt.Circle((0.5, 0.8 - i*0.3), 0.12, color='#2ecc71', alpha=0.2)
    ax2.add_patch(circle)
    ax2.text(0.5, 0.8 - i*0.3, f'-{reduction:.1f}%', ha='center', va='center', fontsize=12, fontweight='bold', color='#27ae60')
    ax2.text(0.5, 0.8 - i*0.3 - 0.16, categories[i], ha='center', va='center', fontsize=10)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('e:/Writing Defence/graphics/lora_efficiency.pdf', format='pdf', bbox_inches='tight')
print("Saved lora_efficiency.pdf")
