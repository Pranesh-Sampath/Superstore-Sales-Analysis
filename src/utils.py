# src/utils.py
import matplotlib.pyplot as plt
import seaborn as sns
import os

OUTPUT_PLOTS = "outputs/plots"
OUTPUT_REPORTS = "outputs/reports"

def save_plot(filename):
    """Save current matplotlib figure to outputs/plots/"""
    os.makedirs(OUTPUT_PLOTS, exist_ok=True)
    plt.savefig(os.path.join(OUTPUT_PLOTS, filename), bbox_inches='tight', dpi=150)
    plt.show()

def set_style():
    """Apply consistent visual theme"""
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams["figure.figsize"] = (12, 5)
    plt.rcParams["axes.titlesize"] = 14
    plt.rcParams["axes.labelsize"] = 12

def save_report(text, filename="summary.md"):
    """Save a markdown report to outputs/reports/"""
    os.makedirs(OUTPUT_REPORTS, exist_ok=True)
    with open(os.path.join(OUTPUT_REPORTS, filename), "w") as f:
        f.write(text)
    print(f"Report saved: {OUTPUT_REPORTS}/{filename}")
