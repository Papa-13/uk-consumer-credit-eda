"""
src/plot_utils.py
─────────────────
Reusable chart styling helpers for consistent visuals across all notebooks.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# ── Brand palette ──────────────────────────────────────────────────────────────
PALETTE   = ['#2563EB', '#DC2626', '#16A34A', '#D97706', '#7C3AED']
GREY_DARK = '#374151'
GREY_MID  = '#9CA3AF'

def apply_style():
    """Apply consistent chart style across all notebooks."""
    plt.rcParams.update({
        'figure.figsize':    (12, 5),
        'font.family':       'DejaVu Sans',
        'axes.spines.top':   False,
        'axes.spines.right': False,
        'axes.grid':         True,
        'grid.alpha':        0.3,
        'grid.linestyle':    '--',
    })
    sns.set_palette(PALETTE)


def add_value_labels(ax, fmt='{:.1f}%', offset=0.3, fontsize=9):
    """Add value labels on top of bar chart bars."""
    for bar in ax.patches:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + offset,
            fmt.format(bar.get_height()),
            ha='center', va='bottom', fontsize=fontsize, fontweight='bold'
        )


def save_fig(fig, filename: str, dpi: int = 150):
    """Save figure to outputs/figures/ folder."""
    path = f'../outputs/figures/{filename}'
    fig.savefig(path, dpi=dpi, bbox_inches='tight')
    print(f'Saved → {path}')


def format_gbp(ax, axis='y'):
    """Format axis ticks as £Xbn."""
    formatter = mticker.FuncFormatter(lambda x, _: f'£{x:.0f}bn')
    if axis == 'y':
        ax.yaxis.set_major_formatter(formatter)
    else:
        ax.xaxis.set_major_formatter(formatter)
