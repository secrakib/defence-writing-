import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import scienceplots

# Apply SciencePlots style for Elsevier (Science journal) quality
plt.style.use(['science', 'no-latex'])
# Tweak some parameters for higher resolution and modern aesthetic
plt.rcParams.update({
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'font.family': 'serif',
    'legend.fontsize': 9
})

os.makedirs('../graphics', exist_ok=True)

# 1. Load Data for Coverage Matrix
df = pd.read_excel('../dataset/Final_For_Defence_V1.xlsx')
cols = list(df.columns)
n = len(cols)

DIALECT_LABELS = {
    'bangla_speech': 'Standard',
    'sylhet_bangla_speech': 'Sylheti',
    'chittagong_bangla_speech': 'Chittagonian',
    'barishal_bangla_speech': 'Barisali',
    'mymensingh_bangla_speech': 'Mymensingh',
    'noakhali_bangla_speech': 'Noakhali',
    'rangpur_bangla_speech': 'Rangpuri',
    'rajshahi_bangla_speech': 'Rajshahi',
    'kishorgonj_bangla_speech': 'Kishoreganj',
    'narail_bangla_speech': 'Narail',
    'narsingdi_bangla_speech': 'Narsingdi',
    'tangail_bangla_speech': 'Tangail',
}
short_labels = [DIALECT_LABELS.get(c, c) for c in cols]

overlap_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        overlap_matrix[i, j] = df[[cols[i], cols[j]]].dropna().shape[0]

# Generate Heatmap (Figure 3)
fig, ax = plt.subplots(figsize=(8, 6))
# Create mask for upper triangle
mask = np.triu(np.ones_like(overlap_matrix, dtype=bool))
sns.heatmap(overlap_matrix, mask=mask, cmap='YlGnBu', annot=True, fmt='.0f', 
            cbar_kws={'label': 'Shared Parallel Pairs'}, 
            xticklabels=short_labels, yticklabels=short_labels, 
            ax=ax, annot_kws={'size': 7}, linewidths=.5)
ax.set_title('Cross-Dialect Parallel Coverage Matrix', pad=15)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('../graphics/coverage_matrix_advanced.png')
plt.close()

# 2. Generate Stacked Bar Chart for Source Contributions (Combining Fig 2 and Fig 3)
# Data provided from the notebook and user prompt
source_data = {
    'Ancholik-NER':  [3481, 3481, 3481, 3481, 3481, 0, 0, 0, 0, 0, 0],
    'Anubhuti':      [2500, 2500, 0, 2500, 0, 0, 0, 2500, 0, 0, 0],
    'BanglaDial':    [442, 577, 790, 712, 0, 655, 891, 0, 0, 0, 0],
    'BhasaBodh':     [980, 980, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'ChatgaiyyaAlap':[0, 4011, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'ONUBAD':        [980, 980, 980, 0, 0, 0, 0, 0, 0, 0, 0],
    'Vashantor':     [2500, 2500, 0, 2500, 2500, 0, 0, 2500, 0, 0, 0],
    'Manual Creation': [0, 0, 0, 0, 0, 500, 0, 500, 500, 500, 500] # Added manual pairs
}

dialects_for_chart = ['Sylheti', 'Chittagonian', 'Barisali', 'Mymensingh',
                       'Noakhali', 'Rangpuri', 'Rajshahi', 'Kishoreganj',
                       'Narail', 'Narsingdi', 'Tangail']

# Convert to DataFrame for easier plotting
df_sources = pd.DataFrame(source_data, index=dialects_for_chart)
# Sort by total volume
df_sources['Total'] = df_sources.sum(axis=1)
df_sources = df_sources.sort_values(by='Total', ascending=True)
totals = df_sources['Total']
df_sources = df_sources.drop(columns=['Total'])

# Professional Color Palette
colors = sns.color_palette("Set2", n_colors=len(df_sources.columns))

fig, ax = plt.subplots(figsize=(10, 6))
bottom = np.zeros(len(df_sources))

for i, col in enumerate(df_sources.columns):
    values = df_sources[col].values
    ax.barh(df_sources.index, values, left=bottom, label=col, color=colors[i], edgecolor='white', linewidth=0.5)
    bottom += values

# Add total labels
for i, total in enumerate(totals):
    ax.text(total + 100, i, f'{int(total):,}', va='center', fontsize=9, fontweight='bold', color='#333333')

ax.set_xlabel('Number of Sentence Pairs')
ax.set_ylabel('Regional Variants')
ax.set_title('Dataset Composition: Source Corpus Contributions and Imbalance Analysis')
ax.legend(title='Source Corpus', bbox_to_anchor=(1.05, 1), loc='upper left')

# Optimize layout
sns.despine(left=True, bottom=True)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('../graphics/source_contributions_advanced.png')
plt.close()

print("High-quality figures generated successfully.")
