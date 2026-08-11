import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_viz():
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.patch.set_facecolor('white')

    # Font settings
    plt.rcParams.update({'font.size': 12, 'font.family': 'sans-serif'})

    colors = {
        'pretrained': '#E6F0FA',
        'trainable': '#FFE6E6',
        'border': '#333333',
        'text': '#000000',
        'arrow': '#666666',
        'math': '#000080'
    }

    # Helper function to draw a box
    def draw_box(ax, x, y, w, h, text, color, fontsize=12):
        rect = patches.Rectangle((x, y), w, h, linewidth=1.5, edgecolor=colors['border'], facecolor=color, zorder=2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize, color=colors['text'], zorder=3)
        return rect

    # Helper function to draw arrow
    def draw_arrow(ax, x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color=colors['arrow']), zorder=1)

    # --- LEFT: LoRA ---
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title("Standard LoRA", fontsize=16, fontweight='bold', pad=20)

    # Input
    ax.text(5, 9.5, "Input $x$", ha='center', va='center', fontsize=14)
    draw_arrow(ax, 5, 9.2, 5, 8.5)
    draw_arrow(ax, 5, 9.2, 2.5, 8.5)
    draw_arrow(ax, 5, 9.2, 7.5, 8.5)

    # Pretrained W
    draw_box(ax, 1, 5, 3, 3.5, "Pretrained Weights\n$W_0 \\in \\mathbb{R}^{d \\times k}$\n(Frozen)", colors['pretrained'])
    
    # LoRA A and B
    draw_box(ax, 6, 7.0, 3, 1.5, "LoRA Matrix $A$\n$\\in \\mathbb{R}^{r \\times k}$", colors['trainable'])
    draw_box(ax, 6, 5, 3, 1.5, "LoRA Matrix $B$\n$\\in \\mathbb{R}^{d \\times r}$", colors['trainable'])
    draw_arrow(ax, 7.5, 7.0, 7.5, 6.5)

    # Outputs
    draw_arrow(ax, 2.5, 5, 2.5, 3.5)
    draw_arrow(ax, 7.5, 5, 7.5, 3.5)

    # Addition
    circle = patches.Circle((5, 3.5), 0.4, linewidth=1.5, edgecolor=colors['border'], facecolor='white', zorder=2)
    ax.add_patch(circle)
    ax.text(5, 3.5, "+", ha='center', va='center', fontsize=18, fontweight='bold', zorder=3)
    
    draw_arrow(ax, 2.5, 3.5, 4.6, 3.5)
    draw_arrow(ax, 7.5, 3.5, 5.4, 3.5)
    
    draw_arrow(ax, 5, 3.1, 5, 2.0)
    ax.text(5, 1.5, "Output $h = xW_0 + xBA$", ha='center', va='center', fontsize=14)

    # Formula
    ax.text(5, 0.5, "Weight Update: $W = W_0 + \\Delta W$\n$\\Delta W = B A$", ha='center', va='center', fontsize=14, color=colors['math'], bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5'))


    # --- RIGHT: DoRA ---
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title("Weight-Decomposed LoRA (DoRA)", fontsize=16, fontweight='bold', pad=20)

    # Pretrained W0 and LoRA delta W
    draw_box(ax, 1, 7.5, 8, 1.5, "Pretrained $W_0$ + LoRA $BA$\n(Direction Component $V = W_0 + B A$)", '#F5F5F5')
    
    # Internal to V
    draw_box(ax, 1.5, 7.7, 3, 1.0, "$W_0$ (Frozen)", colors['pretrained'], fontsize=10)
    draw_box(ax, 5.5, 7.7, 3, 1.0, "$B A$ (Trainable)", colors['trainable'], fontsize=10)
    ax.text(5.0, 8.2, "+", ha='center', va='center', fontsize=14)

    # Normalization
    draw_arrow(ax, 5, 7.5, 5, 6.5)
    draw_box(ax, 3, 5.5, 4, 1.0, "Normalization\n$\\frac{V}{\\|V\\|_c}$", '#FFF0E6')

    # Magnitude
    draw_box(ax, 7.5, 5.5, 1.5, 1.0, "Magnitude $m$\n(Trainable)", colors['trainable'], fontsize=10)

    # Multiplication
    draw_arrow(ax, 5, 5.5, 5, 4.5)
    draw_arrow(ax, 8.25, 5.5, 8.25, 4.5)
    
    circle2 = patches.Circle((5, 4.5), 0.4, linewidth=1.5, edgecolor=colors['border'], facecolor='white', zorder=2)
    ax.add_patch(circle2)
    ax.text(5, 4.5, "$\\otimes$", ha='center', va='center', fontsize=18, fontweight='bold', zorder=3)
    
    draw_arrow(ax, 8.25, 4.5, 5.4, 4.5)

    # Output W
    draw_arrow(ax, 5, 4.1, 5, 3.5)
    draw_box(ax, 2, 2.5, 6, 1.0, "Updated Weights $W$", '#E6FFE6')

    # Formula
    ax.text(5, 0.5, "Weight Update: $W = m \\frac{W_0 + B A}{\\|W_0 + B A\\|_c}$", ha='center', va='center', fontsize=14, color=colors['math'], bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5'))


    plt.tight_layout()
    # plt.savefig('e:\\Writing Defence\\graphics\\dora_vs_lora.pdf', bbox_inches='tight', dpi=300)
    print("Saved graphics/dora_vs_lora.pdf")

if __name__ == '__main__':
    create_viz()
