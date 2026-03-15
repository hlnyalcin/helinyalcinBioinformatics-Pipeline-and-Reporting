Bioinformatics Pipeline for Long-Read FASTAQ Analysis

This project was developed as part of a bioinformatics case study.  
The aim of the pipeline is to perform quality control analysis on long-read sequencing data and provide clear summary outputs before downstream analysis.

The workflow was implemented using **Snakemake** and Python scripts.

---

## Project Overview

The pipeline takes a FASTQ file as input and performs the following steps:

1. Runs **NanoPlot** for long-read quality control
2. Calculates per-read statistics using a custom Python script:
   - GC content
   - Read length
   - Mean read quality score
3. Saves the results in CSV format
4. Generates plots to visualize:
   - GC content distribution
   - Read length distribution
   - Mean read quality score distribution
5. Produces summary statistics for all three metrics

---

## Repository Structure

```text
nanopore_project
│
├── Snakefile
├── environment.yml
├── README.md
│
├── scripts
│   ├── analyze_fastq.py
│   ├── filter_fastq.py
│   ├── filter_high_quality.py
│   ├── plot_distributions.py
│   └── visualize_stats.py
│
├── results
│   ├── read_stats.csv
│   ├── summary_stats.txt
│   └── qc
│
├── figures
│   ├── gc_distribution.png
│   ├── read_length_distribution.png
│   └── quality_distribution.png
│
└── communication
    └── email_to_professor.md

---

## Input Data

The pipeline is designed for long-read sequencing data in FASTQ format.

The original FASTQ file used in this project was too large to upload directly to GitHub, so it was processed locally.

---

## How to Run the Pipeline

1. Create the Conda environment

conda env create -f environment.yml

2. Activate the environment

conda activate nanopore-qc

3. Run the Snakemake workflow

snakemake --cores 4

---

## Main Outputs

QC results are stored in:

results/qc/

Read statistics are stored in:

results/read_stats.csv

This file contains:
- Read_ID
- Read_Length
- GC_Content
- Mean_Quality

Summary statistics are stored in:

results/summary_stats.txt

Figures are stored in:

figures/

Generated plots include:
- gc_distribution.png
- read_length_distribution.png
- quality_distribution.png

---

## QC Tool Used

This project uses NanoPlot, which is designed for long-read sequencing data such as Oxford Nanopore.

---

## Brief Interpretation of Results

The plots show the distributions of GC content, read lengths, and mean read quality scores. These outputs help evaluate sequencing quality before downstream analysis such as alignment.

---
## Author

This repository was prepared for a mini bioinformatics pipeline case study.
