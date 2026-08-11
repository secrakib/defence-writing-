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
    'axes.grid': True,
    'grid.alpha': 0.4
})

# Data
metrics = ['Peak RAM (GB)', 'Avg Latency (ms)', 'Throughput (tok/s)', 'BLEU Score']
fp32_vals = [4.3, 3200, 8.3, 29.26]
int8_vals = [1.5, 900, 26.56, 29.18] # Values based on text

# Normalize data to 0-1 range for radar chart
def normalize(vals, max_vals):
    return [v / m for v, m in zip(vals, max_vals)]

max_vals = [5.0, 4000, 30.0, 35.0]
fp32_norm = normalize(fp32_vals, max_vals)
int8_norm = normalize(int8_vals, max_vals)

# Angles for radar chart
angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
fp32_norm += fp32_norm[:1]
int8_norm += int8_norm[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Draw FP32
ax.plot(angles, fp32_norm, color='#e74c3c', linewidth=2, linestyle='solid', label='FP32 (Original)')
ax.fill(angles, fp32_norm, color='#e74c3c', alpha=0.1)

# Draw INT8
ax.plot(angles, int8_norm, color='#2ecc71', linewidth=2, linestyle='solid', label='INT8 (Quantized)')
ax.fill(angles, int8_norm, color='#2ecc71', alpha=0.25)

# Formatting
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(metrics, fontweight='bold', fontsize=11)
ax.set_yticks([]) # Hide radial ticks

# Annotate values
for i, angle in enumerate(angles[:-1]):
    ha = 'left' if 0 <= angle < np.pi else 'right'
    if angle == 0 or angle == np.pi: ha = 'center'
    
    # FP32 Text
    ax.text(angle, fp32_norm[i] + 0.1, f'{fp32_vals[i]}', color='#c0392b', ha=ha, va='center', fontweight='bold', fontsize=10)
    # INT8 Text
    ax.text(angle, int8_norm[i] + 0.1, f'{int8_vals[i]}', color='#27ae60', ha=ha, va='center', fontweight='bold', fontsize=10)

plt.title('Performance Trade-offs: FP32 vs INT8 Quantization', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
# plt.savefig('e:/Writing Defence/graphics/quantization_radar.pdf', format='pdf', bbox_inches='tight')
print("Saved quantization_radar.pdf")
