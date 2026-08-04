import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('e:/Writing Defence/graphics', exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'figure.dpi': 300,
    'axes.grid': True,
    'grid.alpha': 0.3
})

# Data for the timeline
datasets = ['BdRegionText', 'Vashantor', 'ONUBAD', 'Anubhuti', 'BanglaDial', 'BhasaBodh', 'Proposed (Ours)']
years = [2022, 2023, 2025, 2026, 2025, 2025, 2026]
num_dialects = [4, 5, 3, 4, 11, 2, 11]
# X offsets to prevent overlapping years
years_adj = [2022, 2023, 2024.7, 2025.7, 2025.0, 2025.3, 2026.3] 

# Size proportional to dataset size/impact
sizes = [2573/10, 32500/10, 7950/10, 10000/10, 60729/10, 1960/10, 51531/10]

fig, ax = plt.subplots(figsize=(10, 5))

# Draw the main timeline axis
ax.axhline(0, color='black', linewidth=1.5, alpha=0.8)

# Plot each dataset as a stem/lollipop
colors = ['#95a5a6', '#3498db', '#f39c12', '#9b59b6', '#e67e22', '#1abc9c', '#e74c3c']
y_levels = [1, -1, 2, -2, 3, -1.5, 4]

for i in range(len(datasets)):
    ax.vlines(years_adj[i], 0, y_levels[i], color=colors[i], linestyle='-', linewidth=2, alpha=0.7)
    ax.scatter(years_adj[i], y_levels[i], s=sizes[i]/10, color=colors[i], edgecolor='black', linewidth=1.2, zorder=5)
    
    # Text annotation
    ha = 'center'
    va = 'bottom' if y_levels[i] > 0 else 'top'
    y_offset = 0.2 if y_levels[i] > 0 else -0.2
    
    label = f"{datasets[i]}\n({years[i]}, {num_dialects[i]} Dialects)"
    if datasets[i] == 'Proposed (Ours)':
        label = f"**{datasets[i]}**\n({years[i]}, {num_dialects[i]} Dialects)"
        
    ax.text(years_adj[i], y_levels[i] + y_offset, label, ha=ha, va=va, fontsize=10, 
            bbox=dict(facecolor='white', edgecolor=colors[i], alpha=0.8, boxstyle='round,pad=0.3'))

ax.set_ylim(-3.5, 5.5)
ax.set_xlim(2021.5, 2027)

# Format X axis as years
ax.set_xticks([2022, 2023, 2024, 2025, 2026])
ax.set_xticklabels(['2022', '2023', '2024', '2025', '2026'])
ax.set_yticks([])
ax.set_title('Evolution of Bangla Regional Dialect NLP Datasets', pad=20)

ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.savefig('e:/Writing Defence/graphics/dataset_timeline.pdf', format='pdf', bbox_inches='tight')
print("Saved dataset_timeline.pdf")
