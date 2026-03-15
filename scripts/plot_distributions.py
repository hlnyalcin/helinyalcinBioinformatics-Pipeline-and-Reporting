import os
import pandas as pd
import matplotlib.pyplot as plt

if "snakemake" in globals():
    input_csv = snakemake.input[0]
    out_gc = snakemake.output[0]
    out_length = snakemake.output[1]
    out_quality = snakemake.output[2]
    out_summary = snakemake.output[3]
else:
    input_csv = "results/read_stats.csv"
    out_gc = "figures/gc_distribution.png"
    out_length = "figures/read_length_distribution.png"
    out_quality = "figures/quality_distribution.png"
    out_summary = "results/summary_stats.txt"

os.makedirs(os.path.dirname(out_gc), exist_ok=True)
os.makedirs(os.path.dirname(out_summary), exist_ok=True)

df = pd.read_csv(input_csv)

gc_col = "GC_Content"
length_col = "Read_Length"
quality_col = "Mean_Quality"

summary = {
    "GC Content": {
        "mean": df[gc_col].mean(),
        "median": df[gc_col].median(),
        "min": df[gc_col].min(),
        "max": df[gc_col].max(),
    },
    "Read Length": {
        "mean": df[length_col].mean(),
        "median": df[length_col].median(),
        "min": df[length_col].min(),
        "max": df[length_col].max(),
    },
    "Mean Quality": {
        "mean": df[quality_col].mean(),
        "median": df[quality_col].median(),
        "min": df[quality_col].min(),
        "max": df[quality_col].max(),
    },
}

with open(out_summary, "w", encoding="utf-8") as f:
    for metric, stats in summary.items():
        f.write(f"{metric}\n")
        for key, value in stats.items():
            f.write(f"  {key}: {value:.2f}\n")
        f.write("\n")

print("Özet istatistikler:")
for metric, stats in summary.items():
    print(metric)
    for key, value in stats.items():
        print(f"  {key}: {value:.2f}")
    print()

plt.figure(figsize=(8, 5))
plt.hist(df[gc_col], bins=40, edgecolor="black")
plt.xlabel("GC Content (%)")
plt.ylabel("Read Count")
plt.title("GC Content Distribution")
plt.tight_layout()
plt.savefig(out_gc, dpi=300)
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(df[length_col], bins=40, edgecolor="black")
plt.xlabel("Read Length")
plt.ylabel("Read Count")
plt.title("Read Length Distribution")
plt.tight_layout()
plt.savefig(out_length, dpi=300)
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(df[quality_col], bins=40, edgecolor="black")
plt.xlabel("Mean Read Quality Score")
plt.ylabel("Read Count")
plt.title("Mean Read Quality Distribution")
plt.tight_layout()
plt.savefig(out_quality, dpi=300)
plt.close()