import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('e:/Writing Defence/graphics', exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 13,
    'axes.titlesize': 15,
    'figure.dpi': 300,
    'axes.axisbelow': True
})

error_types = ['Morphological Inflection', 'Lexical Mismatch', 'Syntactic Reordering', 'Partial Translation', 'Hallucination']
percentages = [38, 26, 18, 12, 6]
colors = ['#34495e', '#2980b9', '#27ae60', '#f39c12', '#e74c3c']

fig, ax = plt.subplots(figsize=(8, 5))
y_pos = np.arange(len(error_types))

bars = ax.barh(y_pos, percentages, align='center', color=colors, edgecolor='black', linewidth=1.2)
ax.set_yticks(y_pos)
ax.set_yticklabels(error_types)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Percentage of Analyzed Failure Cases (%)')
ax.set_title('Taxonomy of Translation Errors (N=200 High-TER Cases)')

# Annotate bars
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}%', 
            ha='left', va='center', fontweight='bold', fontsize=11)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', linestyle='--', alpha=0.5)
ax.set_xlim(0, 45)

plt.tight_layout()
plt.savefig('e:/Writing Defence/graphics/error_taxonomy.pdf', format='pdf', bbox_inches='tight')
print("Saved error_taxonomy.pdf")
