import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('e:/Writing Defence/graphics', exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 13,
    'axes.titlesize': 15,
    'legend.fontsize': 11,
    'figure.dpi': 300,
    'axes.grid': True,
    'grid.alpha': 0.3
})

# Dialects and data
dialects = ['Mymensingh', 'Barisali', 'Noakhali', 'Sylheti', 'Chittagonian']
# Estimated distance (arbitrary scale for visualization 1-10)
distances = [2.5, 3.8, 5.5, 8.2, 9.0] 
# Dialect to SCB BLEU (approximate from text)
bleu_d_scb = [55.0, 50.1, 48.0, 45.65, 42.76] 
# SCB to Dialect BLEU (approximate from text)
bleu_scb_d = [45.0, 37.9, 36.5, 33.2, 30.5]
# Training data volume (bubble size)
volumes = [5712, 4270, 5000, 6422, 10567]
bubble_sizes = [v / 10 for v in volumes]

fig, ax = plt.subplots(figsize=(8, 6))

# Scatter plots
scatter1 = ax.scatter(distances, bleu_d_scb, s=bubble_sizes, alpha=0.7, color='#2ecc71', edgecolors='black', linewidth=1.5, label='Dialect → SCB')
scatter2 = ax.scatter(distances, bleu_scb_d, s=bubble_sizes, alpha=0.7, color='#3498db', edgecolors='black', linewidth=1.5, label='SCB → Dialect')

# Annotations
for i, txt in enumerate(dialects):
    ax.annotate(txt, (distances[i], bleu_d_scb[i]), xytext=(0, 15), textcoords='offset points', ha='center', fontsize=9, fontweight='bold')
    ax.annotate(txt, (distances[i], bleu_scb_d[i]), xytext=(0, -20), textcoords='offset points', ha='center', fontsize=9)

# Trendlines
z1 = np.polyfit(distances, bleu_d_scb, 1)
p1 = np.poly1d(z1)
ax.plot(distances, p1(distances), color='#2ecc71', linestyle='--', alpha=0.8)

z2 = np.polyfit(distances, bleu_scb_d, 1)
p2 = np.poly1d(z2)
ax.plot(distances, p2(distances), color='#3498db', linestyle='--', alpha=0.8)

# Formatting
ax.set_xlabel('Linguistic/Morphological Distance from Standard Bangla (SCB)')
ax.set_ylabel('Translation Quality (BLEU Score)')
ax.set_title('Impact of Linguistic Proximity on Translation Quality')
ax.set_xlim(1, 10)
ax.set_ylim(20, 60)

# Custom legend for bubble size
handles, labels = ax.get_legend_handles_labels()
l1 = plt.scatter([],[], s=400, color='gray', alpha=0.5, edgecolors='black', label='~4,000 Pairs')
l2 = plt.scatter([],[], s=1000, color='gray', alpha=0.5, edgecolors='black', label='~10,000 Pairs')
handles.extend([l1, l2])

ax.legend(handles=handles, loc='upper right', frameon=True, framealpha=0.9, edgecolor='black')

plt.tight_layout()
plt.savefig('e:/Writing Defence/graphics/proximity_vs_bleu.pdf', format='pdf', bbox_inches='tight')
print("Saved proximity_vs_bleu.pdf")
