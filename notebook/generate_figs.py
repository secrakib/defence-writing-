import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import warnings
warnings.filterwarnings('ignore')
import os

os.makedirs('../graphics', exist_ok=True)

# --- Professional Styling ---
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'figure.dpi': 200,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'figure.facecolor': 'white',
})

# Color palette
COLORS = {
    'primary': '#2563EB',
    'secondary': '#7C3AED',
    'accent': '#059669',
    'warning': '#D97706',
    'danger': '#DC2626',
    'dark': '#1E293B',
    'light': '#F8FAFC',
    'muted': '#94A3B8',
}

DIALECT_COLORS = {
    'bangla_speech': '#2563EB',
    'sylhet_bangla_speech': '#7C3AED',
    'chittagong_bangla_speech': '#DC2626',
    'barishal_bangla_speech': '#059669',
    'mymensingh_bangla_speech': '#D97706',
    'noakhali_bangla_speech': '#0891B2',
    'rangpur_bangla_speech': '#BE185D',
    'rajshahi_bangla_speech': '#4338CA',
    'kishorgonj_bangla_speech': '#9333EA',
    'narail_bangla_speech': '#65A30D',
    'narsingdi_bangla_speech': '#EA580C',
    'tangail_bangla_speech': '#0D9488',
}

DIALECT_LABELS = {
    'bangla_speech': 'Standard Bangla',
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

print('Setup complete.')

df = pd.read_excel('../dataset/Final_For_Defence_V1.xlsx')
print(f'Dataset Shape: {df.shape[0]:,} rows × {df.shape[1]} columns')
print(f'Total Non-null Cells: {df.count().sum():,}')
print()
print('Columns:', list(df.columns))
print()
print('Non-null counts per dialect:')
for col in df.columns:
    label = DIALECT_LABELS.get(col, col)
    cnt = df[col].count()
    pct = cnt / len(df) * 100
    print(f'  {label:>18s}: {cnt:>6,} ({pct:5.1f}%)')

# --- Fig 1: Dialect Sample Distribution ---
fig, ax = plt.subplots(figsize=(12, 6))

counts = df.count().sort_values(ascending=True)
labels = [DIALECT_LABELS.get(c, c) for c in counts.index]
colors = [DIALECT_COLORS.get(c, '#94A3B8') for c in counts.index]

bars = ax.barh(range(len(counts)), counts.values, color=colors, edgecolor='white', linewidth=0.5, height=0.7)

# Add value labels
for i, (val, bar) in enumerate(zip(counts.values, bars)):
    ax.text(val + 150, i, f'{val:,}', va='center', ha='left', fontsize=10, fontweight='bold', color=COLORS['dark'])

ax.set_yticks(range(len(counts)))
ax.set_yticklabels(labels, fontsize=11)
ax.set_xlabel('Number of Sentences', fontsize=12, fontweight='bold')
ax.set_title('Dialect Coverage: Severe Imbalance Across Regional Variants', fontsize=14, fontweight='bold', pad=15)
ax.set_xlim(0, max(counts.values) * 1.2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add imbalance ratio annotation
ratio = counts.values[-1] / counts.values[0]
ax.annotate(f'Max/Min Ratio: {ratio:.1f}×', xy=(0.75, 0.05), xycoords='axes fraction',
            fontsize=12, fontweight='bold', color=COLORS['danger'],
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FEE2E2', edgecolor=COLORS['danger'], alpha=0.9))

plt.tight_layout()
plt.savefig('../graphics/dialect_coverage.png')
print('Saved: graphics/dialect_coverage.png')
plt.show()

# --- Fig 2: Sentence Length Violin Plot ---
fig, ax = plt.subplots(figsize=(14, 6))

# Select major dialects for cleaner visualization
major_dialects = ['bangla_speech', 'sylhet_bangla_speech', 'chittagong_bangla_speech',
                  'barishal_bangla_speech', 'mymensingh_bangla_speech', 'noakhali_bangla_speech',
                  'rangpur_bangla_speech', 'rajshahi_bangla_speech']

length_data = []
for col in major_dialects:
    lengths = df[col].dropna().astype(str).str.len()
    length_data.append(lengths.values)

parts = ax.violinplot(length_data, positions=range(len(major_dialects)), showmeans=True, showmedians=True)

for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(DIALECT_COLORS[major_dialects[i]])
    pc.set_alpha(0.7)

parts['cmeans'].set_color(COLORS['danger'])
parts['cmedians'].set_color(COLORS['dark'])

ax.set_xticks(range(len(major_dialects)))
ax.set_xticklabels([DIALECT_LABELS[d] for d in major_dialects], rotation=30, ha='right', fontsize=10)
ax.set_ylabel('Sentence Length (characters)', fontsize=12, fontweight='bold')
ax.set_title('Sentence Length Distribution: Structural Variation Across Dialects', fontsize=14, fontweight='bold', pad=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, 200)

# Legend
from matplotlib.lines import Line2D
legend_elements = [Line2D([0],[0], color=COLORS['danger'], lw=2, label='Mean'),
                   Line2D([0],[0], color=COLORS['dark'], lw=2, label='Median')]
ax.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.savefig('../graphics/sentence_lengths.png')
print('Saved: graphics/sentence_lengths.png')
plt.show()

# --- Fig 3: Source Corpus Contributions (from idea.md data) ---
source_data = {
    'Ancholik-NER':  [3481, 3481, 3481, 3481, 3481, 0, 0, 0, 0, 0, 0],
    'Anubhuti':      [2500, 2500, 0, 2500, 0, 0, 0, 2500, 0, 0, 0],
    'BanglaDial':    [442, 577, 790, 712, 0, 655, 891, 0, 0, 0, 0],
    'BhasaBodh':     [980, 980, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'ChatgaiyyaAlap':[0, 4011, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'ONUBAD':        [980, 980, 980, 0, 0, 0, 0, 0, 0, 0, 0],
    'Vashantor':     [2500, 2500, 0, 2500, 2500, 0, 0, 2500, 0, 0, 0],
}

dialects_for_chart = ['Sylheti', 'Chittagonian', 'Barisali', 'Mymensingh',
                       'Noakhali', 'Rangpuri', 'Rajshahi', 'Kishoreganj',
                       'Narail', 'Narsingdi', 'Tangail']

source_colors = ['#2563EB', '#7C3AED', '#059669', '#D97706', '#DC2626', '#0891B2', '#BE185D']

fig, ax = plt.subplots(figsize=(14, 7))

x = np.arange(len(dialects_for_chart))
width = 0.6
bottom = np.zeros(len(dialects_for_chart))

for idx, (source, values) in enumerate(source_data.items()):
    ax.bar(x, values, width, bottom=bottom, label=source, color=source_colors[idx], edgecolor='white', linewidth=0.5)
    bottom += np.array(values)

# Add total labels on top
for i, total in enumerate(bottom):
    if total > 0:
        ax.text(i, total + 100, f'{int(total):,}', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(dialects_for_chart, rotation=35, ha='right', fontsize=10)
ax.set_ylabel('Number of Sentence Pairs', fontsize=12, fontweight='bold')
ax.set_title('Source Corpus Contribution per Dialect', fontsize=14, fontweight='bold', pad=15)
ax.legend(loc='upper right', fontsize=9, framealpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('../graphics/source_contributions.png')
print('Saved: graphics/source_contributions.png')
plt.show()

# --- Fig 4: Model Comparison ---
models = ['BanglaT5\n(20 ep)', 'NLLB-200', 'mBART-50', 'BanglaT5\n(100 ep)']
metrics = {
    'BLEU': [23.22, 14.76, 8.96, 29.26],
    'chrF++': [51.20, 42.62, 32.94, 57.26],
    'METEOR': [41.41, 33.56, 23.82, 49.68],
    'TER ↓': [56.85, 64.53, 77.10, 50.59],
}

fig, axes = plt.subplots(1, 4, figsize=(16, 5))
metric_colors = ['#2563EB', '#7C3AED', '#059669', '#DC2626']

for ax, (metric, values), color in zip(axes, metrics.items(), metric_colors):
    bars = ax.bar(range(len(models)), values, color=color, alpha=0.85, edgecolor='white', width=0.65)

    # Highlight best
    if 'TER' in metric:
        best_idx = np.argmin(values)
    else:
        best_idx = np.argmax(values)
    bars[best_idx].set_edgecolor('#FFD700')
    bars[best_idx].set_linewidth(3)

    for i, val in enumerate(values):
        ax.text(i, val + 1, f'{val:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_xticks(range(len(models)))
    ax.set_xticklabels(models, fontsize=8)
    ax.set_title(metric, fontsize=13, fontweight='bold', color=color)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if 'TER' in metric:
        ax.set_ylim(0, 100)
    else:
        ax.set_ylim(0, max(values) * 1.25)

fig.suptitle('Model Performance Comparison (Overall Metrics)', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('../graphics/model_comparison.png')
print('Saved: graphics/model_comparison.png')
plt.show()

# --- Fig 5: Dataset Size vs Performance ---
# LoRA r=8, alpha=16 (Epoch 10)
sizes_r8 = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4499]
bleu_r8 =  [12.09, 14.45, 17.71, 18.28, 19.67, 23.00, 23.99, 25.40, 25.74]
chrf_r8 =  [39.56, 42.95, 46.92, 47.03, 48.57, 52.35, 53.23, 54.40, 54.89]

# LoRA r=64, alpha=128 (Epoch 20)
sizes_r64 = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4499]
bleu_r64 =  [11.47, 17.13, 19.86, 22.50, 23.15, 25.00, 25.83, 26.50, 27.55]
chrf_r64 =  [39.51, 46.10, 49.10, 51.81, 52.48, 54.41, 55.17, 55.79, 56.73]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# BLEU
ax1.plot(sizes_r8, bleu_r8, 'o-', color='#2563EB', linewidth=2.5, markersize=7, label='LoRA r=8, α=16 (10 ep)', zorder=3)
ax1.plot(sizes_r64, bleu_r64, 's-', color='#DC2626', linewidth=2.5, markersize=7, label='LoRA r=64, α=128 (20 ep)', zorder=3)
ax1.fill_between(sizes_r64, bleu_r8, bleu_r64, alpha=0.1, color='#059669')
ax1.set_xlabel('Training Dataset Size (sentences per dialect pair)', fontsize=11, fontweight='bold')
ax1.set_ylabel('BLEU Score', fontsize=12, fontweight='bold')
ax1.set_title('BLEU vs. Training Data Size', fontsize=13, fontweight='bold')
ax1.legend(fontsize=9, loc='lower right')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(True, alpha=0.3)

# chrF++
ax2.plot(sizes_r8, chrf_r8, 'o-', color='#7C3AED', linewidth=2.5, markersize=7, label='LoRA r=8, α=16 (10 ep)', zorder=3)
ax2.plot(sizes_r64, chrf_r64, 's-', color='#D97706', linewidth=2.5, markersize=7, label='LoRA r=64, α=128 (20 ep)', zorder=3)
ax2.fill_between(sizes_r64, chrf_r8, chrf_r64, alpha=0.1, color='#059669')
ax2.set_xlabel('Training Dataset Size (sentences per dialect pair)', fontsize=11, fontweight='bold')
ax2.set_ylabel('chrF++ Score', fontsize=12, fontweight='bold')
ax2.set_title('chrF++ vs. Training Data Size', fontsize=13, fontweight='bold')
ax2.legend(fontsize=9, loc='lower right')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(True, alpha=0.3)

fig.suptitle('Data Scaling Analysis: Performance Improves with Larger Corpora', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('../graphics/dataset_scaling.png')
print('Saved: graphics/dataset_scaling.png')
plt.show()

# --- Fig 6: BLEU Heatmap for BanglaT5 100-epoch (best model) ---
# Extract dialect→dialect BLEU from baseline_results.md (100 epochs)
dialect_names_short = ['SCB', 'Barishal', 'Chittagong', 'Mymensingh', 'Noakhali',
                       'Rajshahi', 'Rangpur', 'Sylhet']

# BLEU matrix: rows=source, cols=target (from BanglaT5 100ep results)
# Order: SCB, Barishal, Chittagong, Mymensingh, Noakhali, Rajshahi, Rangpur, Sylhet
bleu_matrix = np.array([
    [np.nan, 37.87, 28.46, 39.96, 29.45, 7.91, 11.52, 29.49],   # SCB→
    [50.10, np.nan, 15.82, 35.55, 23.16, 5.57, 11.42, 21.63],   # Barishal→
    [42.76, 27.89, np.nan, 20.83, 18.75, 7.14, 11.78, 19.22],   # Chittagong→
    [55.00, 36.70, 19.32, np.nan, 27.71, 6.26, 11.00, 25.51],   # Mymensingh→
    [41.39, 33.78, 19.33, 28.20, np.nan, np.nan, np.nan, 21.55], # Noakhali→
    [23.40, 6.79, 8.45, 10.19, np.nan, np.nan, 7.09, 13.35],    # Rajshahi→
    [23.39, 11.76, 11.33, 11.10, np.nan, 5.55, np.nan, 16.43],  # Rangpur→
    [45.65, 32.04, 21.50, 28.21, 23.91, 5.73, 12.27, np.nan],   # Sylhet→
])

fig, ax = plt.subplots(figsize=(10, 8))

# Create masked array for NaN values
masked_matrix = np.ma.masked_invalid(bleu_matrix)
cmap = plt.cm.RdYlGn
cmap.set_bad(color='#F1F5F9')

im = ax.imshow(masked_matrix, cmap=cmap, vmin=0, vmax=60, aspect='auto')

# Add text annotations
for i in range(len(dialect_names_short)):
    for j in range(len(dialect_names_short)):
        if not np.isnan(bleu_matrix[i, j]):
            val = bleu_matrix[i, j]
            color = 'white' if val < 15 or val > 45 else 'black'
            ax.text(j, i, f'{val:.1f}', ha='center', va='center', fontsize=10, fontweight='bold', color=color)
        else:
            ax.text(j, i, '—', ha='center', va='center', fontsize=10, color='#CBD5E1')

ax.set_xticks(range(len(dialect_names_short)))
ax.set_xticklabels(dialect_names_short, rotation=45, ha='right', fontsize=11)
ax.set_yticks(range(len(dialect_names_short)))
ax.set_yticklabels(dialect_names_short, fontsize=11)
ax.set_xlabel('Target Dialect', fontsize=12, fontweight='bold')
ax.set_ylabel('Source Dialect', fontsize=12, fontweight='bold')
ax.set_title('Cross-Dialectal Translation BLEU Scores\n(BanglaT5, 100 Epochs — Best Model)', fontsize=14, fontweight='bold', pad=15)

plt.colorbar(im, ax=ax, label='BLEU Score', shrink=0.8)

plt.tight_layout()
plt.savefig('../graphics/bleu_heatmap.png')
print('Saved: graphics/bleu_heatmap.png')
plt.show()

# --- Fig 7: Directionality Analysis ---
dialects_dir = ['Barishal', 'Chittagong', 'Mymensingh', 'Noakhali', 'Rajshahi', 'Rangpur', 'Sylhet']

# BanglaT5 100-epoch: Dialect→SCB vs SCB→Dialect BLEU
dialect_to_scb = [50.10, 42.76, 55.00, 41.39, 23.40, 23.39, 45.65]
scb_to_dialect = [37.87, 28.46, 39.96, 29.45, 7.91, 11.52, 29.49]

fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(dialects_dir))
width = 0.35

bars1 = ax.bar(x - width/2, dialect_to_scb, width, label='Dialect → Standard Bangla',
               color='#2563EB', edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x + width/2, scb_to_dialect, width, label='Standard Bangla → Dialect',
               color='#DC2626', edgecolor='white', linewidth=0.5)

# Asymmetry arrows
for i, (d2s, s2d) in enumerate(zip(dialect_to_scb, scb_to_dialect)):
    diff = d2s - s2d
    ax.annotate(f'+{diff:.1f}', xy=(i, max(d2s, s2d) + 1.5), ha='center', fontsize=8,
               fontweight='bold', color='#059669')

for i, val in enumerate(dialect_to_scb):
    ax.text(i - width/2, val + 0.5, f'{val:.1f}', ha='center', va='bottom', fontsize=8)
for i, val in enumerate(scb_to_dialect):
    ax.text(i + width/2, val + 0.5, f'{val:.1f}', ha='center', va='bottom', fontsize=8)

ax.set_xticks(x)
ax.set_xticklabels(dialects_dir, fontsize=11)
ax.set_ylabel('BLEU Score', fontsize=12, fontweight='bold')
ax.set_title('Translation Directionality Asymmetry (BanglaT5, 100 Epochs)', fontsize=14, fontweight='bold', pad=15)
ax.legend(fontsize=10, loc='upper right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, 65)

plt.tight_layout()
plt.savefig('../graphics/directionality.png')
print('Saved: graphics/directionality.png')
plt.show()

# --- Fig 8: Dataset Comparison ---
dialects_comp = ['Std Bangla', 'Sylheti', 'Chittagonian', 'Barisali', 'Noakhali',
                 'Mymensingh', 'Rangpuri', 'Rajshahi']
our_data = [13556, 6422, 10567, 4270, 5000, 5712, 1155, 891]
best_competitor = [4011, 3481, 4011, 3481, 2500, 3481, 655, 891]
competitor_name = ['ChatgaiyyaAlap', 'Ancholik-NER', 'ChatgaiyyaAlap', 'Ancholik-NER',
                   'Vashantor', 'Ancholik-NER', 'BanglaDial', 'BanglaDial']

fig, ax = plt.subplots(figsize=(14, 6))

x = np.arange(len(dialects_comp))
width = 0.35

bars1 = ax.bar(x - width/2, our_data, width, label='Our Dataset', color='#2563EB', edgecolor='white')
bars2 = ax.bar(x + width/2, best_competitor, width, label='Best Competitor', color='#94A3B8', edgecolor='white')

# Add multiplier labels
for i, (ours, theirs) in enumerate(zip(our_data, best_competitor)):
    if theirs > 0:
        ratio = ours / theirs
        if ratio > 1:
            ax.text(i, max(ours, theirs) + 200, f'{ratio:.1f}×', ha='center',
                    fontsize=10, fontweight='bold', color='#059669')
        else:
            ax.text(i, max(ours, theirs) + 200, 'Equal', ha='center',
                    fontsize=9, fontweight='bold', color='#94A3B8')

ax.set_xticks(x)
ax.set_xticklabels(dialects_comp, rotation=30, ha='right', fontsize=10)
ax.set_ylabel('Number of Sentences', fontsize=12, fontweight='bold')
ax.set_title('Our Dataset vs. Best Prior Corpus per Dialect', fontsize=14, fontweight='bold', pad=15)
ax.legend(fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('../graphics/dataset_comparison.png')
print('Saved: graphics/dataset_comparison.png')
plt.show()

# --- Fig 9: Parallel Coverage Matrix ---
cols = list(df.columns)
n = len(cols)
labels_short = [DIALECT_LABELS.get(c, c)[:6] for c in cols]

# Compute pairwise non-null overlap
overlap_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        overlap_matrix[i, j] = df[[cols[i], cols[j]]].dropna().shape[0]

fig, ax = plt.subplots(figsize=(12, 10))
im = ax.imshow(overlap_matrix, cmap='YlOrRd', aspect='auto')

for i in range(n):
    for j in range(n):
        val = int(overlap_matrix[i, j])
        color = 'white' if val > 6000 else 'black'
        ax.text(j, i, f'{val:,}', ha='center', va='center', fontsize=7, fontweight='bold', color=color)

short_labels = ['SCB', 'Syl', 'Bar', 'Cht', 'Mym', 'Noa', 'Ran', 'Raj', 'Kis', 'Nar', 'Nrs', 'Tan']
ax.set_xticks(range(n))
ax.set_xticklabels(short_labels, rotation=45, ha='right', fontsize=10)
ax.set_yticks(range(n))
ax.set_yticklabels(short_labels, fontsize=10)
ax.set_title('Cross-Dialect Parallel Coverage\n(Number of Shared Sentence Pairs)', fontsize=14, fontweight='bold', pad=15)

plt.colorbar(im, ax=ax, label='Parallel Pairs', shrink=0.8)
plt.tight_layout()
plt.savefig('../graphics/coverage_matrix.png')
print('Saved: graphics/coverage_matrix.png')
plt.show()

# --- IMPROVED OVERVIEW DIAGRAM ---
fig, ax = plt.subplots(figsize=(18, 11))
ax.set_xlim(0, 18)
ax.set_ylim(0, 11)
ax.axis('off')
fig.patch.set_facecolor('white')

def draw_rounded_box(ax, x, y, w, h, text, facecolor='#EFF6FF', edgecolor='#2563EB',
                     fontsize=10, fontweight='bold', textcolor='#1E293B', alpha=1.0, lw=1.5):
    box = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.15', facecolor=facecolor,
                         edgecolor=edgecolor, linewidth=lw, alpha=alpha, zorder=2)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize,
            fontweight=fontweight, color=textcolor, zorder=3)

def draw_arrow(ax, x1, y1, x2, y2, color='#64748B', lw=1.5, style='->'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw, connectionstyle='arc3,rad=0'))

# === TITLE ===
ax.text(9, 10.6, 'Poly-Dialectal Neural Machine Translation Framework', ha='center', va='center',
        fontsize=16, fontweight='bold', color='#1E293B')
ax.text(9, 10.2, 'End-to-End Architecture: Data Integration → Model Training → Multi-Directional Evaluation',
        ha='center', va='center', fontsize=10, color='#64748B', style='italic')

# === PHASE 1: DATA SOURCES (Left Column) ===
ax.add_patch(FancyBboxPatch((0.3, 2.5), 3.4, 7.3, boxstyle='round,pad=0.2',
             facecolor='#F0FDF4', edgecolor='#059669', linewidth=2, alpha=0.5, zorder=1))
ax.text(2.0, 9.5, 'Phase 1: Source Corpora', ha='center', fontsize=12, fontweight='bold', color='#059669')

sources = [
    ('Ancholik-NER', '3,481 sent × 5 dial'),
    ('Anubhuti', '2,500 sent × 4 dial'),
    ('BanglaDial', '3,452 sent (variable)'),
    ('BhasaBodh', '980 sent × 3 dial'),
    ('ChatgaiyyaAlap', '4,011 sent × 1 dial'),
    ('ONUBAD', '980 sent × 4 dial'),
    ('Vashantor', '2,500 sent × 5 dial'),
]

source_colors_list = ['#DBEAFE', '#E0E7FF', '#D1FAE5', '#FEF3C7', '#FEE2E2', '#CFFAFE', '#F3E8FF']
source_edge_colors = ['#2563EB', '#4338CA', '#059669', '#D97706', '#DC2626', '#0891B2', '#7C3AED']

for i, (name, desc) in enumerate(sources):
    y_pos = 8.6 - i * 0.9
    draw_rounded_box(ax, 0.5, y_pos, 3.0, 0.7, f'{name}\n{desc}',
                     facecolor=source_colors_list[i], edgecolor=source_edge_colors[i],
                     fontsize=8, lw=1.2)

# === PHASE 2: DATA INTEGRATION (Center-Left) ===
ax.add_patch(FancyBboxPatch((4.2, 4.0), 3.0, 5.5, boxstyle='round,pad=0.2',
             facecolor='#EFF6FF', edgecolor='#2563EB', linewidth=2, alpha=0.4, zorder=1))
ax.text(5.7, 9.2, 'Phase 2: Data Pipeline', ha='center', fontsize=12, fontweight='bold', color='#2563EB')

pipeline_steps = [
    ('Integration &\nDeduplication', '#DBEAFE', '#2563EB'),
    ('Unicode\nNormalization', '#E0E7FF', '#4338CA'),
    ('Tokenization &\nScript Alignment', '#DBEAFE', '#2563EB'),
    ('Train / Dev / Test\n(80 / 10 / 10)', '#D1FAE5', '#059669'),
]

for i, (step, fc, ec) in enumerate(pipeline_steps):
    y_pos = 8.3 - i * 1.2
    draw_rounded_box(ax, 4.4, y_pos, 2.6, 0.9, step, facecolor=fc, edgecolor=ec, fontsize=9)
    if i < len(pipeline_steps) - 1:
        draw_arrow(ax, 5.7, y_pos, 5.7, y_pos - 0.3, color=ec)

# Dataset stats box
draw_rounded_box(ax, 4.4, 4.2, 2.6, 0.7,
                 '14,552 rows\n12 dialects | 51,531 pairs',
                 facecolor='#FEF3C7', edgecolor='#D97706', fontsize=9)

# === PHASE 3: MODELS (Center-Right) ===
ax.add_patch(FancyBboxPatch((7.7, 4.0), 3.6, 5.5, boxstyle='round,pad=0.2',
             facecolor='#FDF2F8', edgecolor='#BE185D', linewidth=2, alpha=0.4, zorder=1))
ax.text(9.5, 9.2, 'Phase 3: NMT Models', ha='center', fontsize=12, fontweight='bold', color='#BE185D')

models_info = [
    ('BanglaT5 (247M)', 'Best: BLEU 29.26', '#DBEAFE', '#2563EB'),
    ('NLLB-200 (615M)', 'BLEU 14.76', '#E0E7FF', '#4338CA'),
    ('mBART-50 (611M)', 'BLEU 8.96', '#F3E8FF', '#7C3AED'),
]

for i, (model, score, fc, ec) in enumerate(models_info):
    y_pos = 8.0 - i * 1.3
    draw_rounded_box(ax, 7.9, y_pos, 3.2, 1.0, f'{model}\n{score}',
                     facecolor=fc, edgecolor=ec, fontsize=10)

# LoRA config box
draw_rounded_box(ax, 7.9, 4.2, 3.2, 0.7,
                 'LoRA Fine-tuning\nr=64, α=128, 20 epochs',
                 facecolor='#FEE2E2', edgecolor='#DC2626', fontsize=9)

# === PHASE 4: TRANSLATION DIRECTIONS (Right) ===
ax.add_patch(FancyBboxPatch((11.8, 5.5), 2.8, 4.0, boxstyle='round,pad=0.2',
             facecolor='#FEF9C3', edgecolor='#CA8A04', linewidth=2, alpha=0.4, zorder=1))
ax.text(13.2, 9.2, 'Phase 4: Directions', ha='center', fontsize=12, fontweight='bold', color='#CA8A04')

directions = [
    ('Dialect → SCB', '#D1FAE5', '#059669'),
    ('SCB → Dialect', '#DBEAFE', '#2563EB'),
    ('Dialect ↔ Dialect', '#FEE2E2', '#DC2626'),
]

for i, (direction, fc, ec) in enumerate(directions):
    y_pos = 8.3 - i * 1.1
    draw_rounded_box(ax, 12.0, y_pos, 2.4, 0.8, direction,
                     facecolor=fc, edgecolor=ec, fontsize=10)

# === PHASE 5: EVALUATION (Bottom Right) ===
ax.add_patch(FancyBboxPatch((11.8, 2.0), 5.8, 3.0, boxstyle='round,pad=0.2',
             facecolor='#F5F3FF', edgecolor='#7C3AED', linewidth=2, alpha=0.4, zorder=1))
ax.text(14.7, 4.7, 'Phase 5: Evaluation & Results', ha='center', fontsize=12, fontweight='bold', color='#7C3AED')

eval_metrics = [
    ('BLEU\n29.26', '#DBEAFE', '#2563EB'),
    ('chrF++\n57.26', '#E0E7FF', '#4338CA'),
    ('METEOR\n49.68', '#D1FAE5', '#059669'),
    ('TER\n50.59', '#FEE2E2', '#DC2626'),
]

for i, (metric, fc, ec) in enumerate(eval_metrics):
    x_pos = 12.1 + i * 1.35
    draw_rounded_box(ax, x_pos, 3.5, 1.15, 0.9, metric,
                     facecolor=fc, edgecolor=ec, fontsize=10)

# Key finding box
draw_rounded_box(ax, 12.0, 2.2, 5.4, 0.9,
                 'Key Finding: BanglaT5 achieves +26% BLEU improvement\n'
                 'over 10→100 epochs | Mymensingh→SCB best pair (55.0 BLEU)',
                 facecolor='#FEF3C7', edgecolor='#D97706', fontsize=9, lw=2)

# === CONNECTING ARROWS ===
# Sources → Pipeline
for i in range(7):
    y_pos = 8.95 - i * 0.9
    draw_arrow(ax, 3.5, y_pos, 4.4, 6.8 if i < 4 else 5.6, color='#059669', lw=1)

# Pipeline → Models
draw_arrow(ax, 7.0, 6.5, 7.9, 7.5, color='#2563EB', lw=2)
draw_arrow(ax, 7.0, 5.5, 7.9, 5.5, color='#2563EB', lw=2)

# Models → Directions
draw_arrow(ax, 11.1, 7.5, 12.0, 8.5, color='#CA8A04', lw=2)
draw_arrow(ax, 11.1, 6.5, 12.0, 7.4, color='#CA8A04', lw=2)

# Directions → Evaluation
draw_arrow(ax, 13.2, 5.5, 13.5, 4.7, color='#7C3AED', lw=2)

# === BOTTOM ANNOTATION ===
ax.text(9.0, 0.8, 'Largest poly-dialectal NMT corpus for Bangla: 14,552 aligned sentences across 12 regional variants',
        ha='center', va='center', fontsize=11, fontweight='bold', color='#475569', style='italic')
ax.text(9.0, 0.3, 'Unified architecture enables direct multi-directional translation without pivot-based cascading errors',
        ha='center', va='center', fontsize=10, color='#94A3B8', style='italic')

plt.savefig('../graphics/overview.png', dpi=300, bbox_inches='tight', facecolor='white')
print('Saved: graphics/overview.png (IMPROVED)')
plt.show()

