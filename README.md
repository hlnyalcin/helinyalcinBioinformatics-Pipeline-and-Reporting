 Bioinformatics Pipeline for Long-Read Quality Control

## Project Summary

This repository contains a reproducible bioinformatics workflow developed for a mini case study.  
The aim of this project is to perform quality control analysis on long-read sequencing data and produce clear statistical summaries and visualizations before downstream analysis.

The workflow was implemented using **Snakemake** together with custom **Python scripts**.

---

## Project Goal

The purpose of this pipeline is to analyze a raw long-read sequencing FASTQ file and answer the following questions:

- What is the general quality of the reads?
- What is the read length distribution?
- What is the GC content distribution?
- Are the mean read quality scores sufficient for downstream analysis?

To answer these questions, the pipeline combines a long-read QC tool with custom analysis and visualization scripts.

---

## What the Pipeline Does

The workflow performs the following steps:

1. Takes a FASTQ file as input.
2. Runs **NanoPlot** to generate quality control reports for long-read sequencing data.
3. Uses a custom Python script to calculate, for each individual read:
   - GC content percentage
   - Read length
   - Mean read quality score
4. Saves these values in a structured CSV file.
5. Uses a separate visualization script to generate distribution plots for:
   - GC content
   - Read length
   - Mean read quality score
6. Calculates and saves summary statistics such as:
   - mean
   - median
   - minimum
   - maximum

---

## Why Snakemake Was Used

This project uses **Snakemake** as the workflow management system.

Snakemake makes the analysis reproducible because it:

- defines the workflow in a clear and structured way
- keeps track of inputs and outputs
- allows the pipeline to be rerun in a consistent way
- makes it easy to reproduce the analysis on another machine

---

## Input Data

The input for this workflow is a long-read sequencing file in **FASTQ** format.

Example input:

```text
barcode77.fastq

Because the original FASTQ file is large, it may not always be uploaded directly to GitHub.
However, the workflow is written so that the analysis can be reproduced as long as the input FASTQ file is available locally.

Software and Environment

This project uses a Conda environment to ensure reproducibility.

The required software is defined in:environment.yml
Main tools and libraries used in the project include:

Snakemake

NanoPlot

Python

pandas

matplotlib

Bioinformatics Pipeline for Long-Read Quality Control
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

Pipeline Steps in Detail
Step 1: Quality Control with NanoPlot

The first part of the workflow uses NanoPlot, which is a QC tool specifically designed for long-read sequencing data such as Oxford Nanopore reads.

NanoPlot produces several QC outputs, including:

HTML reports

read length histograms

quality score plots

scatter plots

summary statistics

These files are stored in:Pipeline Steps in Detail
Step 1: Quality Control with NanoPlot

The first part of the workflow uses NanoPlot, which is a QC tool specifically designed for long-read sequencing data such as Oxford Nanopore reads.

NanoPlot produces several QC outputs, including:

HTML reports

read length histograms

quality score plots

scatter plots

summary statistics

These files are stored in:results/qc/
This step provides an overall quality assessment of the sequencing dataset.
Step 2: Read-Level Statistical Analysis

A custom Python script is used to calculate important statistics for each read in the FASTQ file.

The script calculates:

GC_Content

Read_Length

Mean_Quality

The output is saved in:

results/read_stats.csv

This CSV file contains one row per read and includes the following columns:

Read_ID
Read_Length
GC_Content
Mean_Quality

This step is important because it provides a structured dataset that can be used for downstream visualization and interpretation.

Step 3: Data Visualization

A separate visualization script reads the read_stats.csv file and generates plots showing the distributions of the three main metrics.

The generated plots are:

GC content distribution

read length distribution

mean read quality score distribution

These figures are saved in:

figures/

Expected output files include:

figures/gc_distribution.png
figures/read_length_distribution.png
figures/quality_distribution.png
Step 4: Summary Statistics

In addition to the plots, the visualization step also calculates summary statistics for the three metrics.

These include values such as:

mean

median

minimum

maximum

The summary is saved in:

results/summary_stats.txt

This file helps provide a quick overview of the dataset without opening the full CSV file.

How to Run the Pipeline

Follow the steps below to reproduce the analysis.

1. Clone or download the repository

If using Git:

git clone <repository_url>
cd nanopore_project

If downloading manually from GitHub, extract the repository and open the project folder.

2. Create the Conda environment

Run the following command:

conda env create -f environment.yml

This command will install all required dependencies listed in the environment.yml file.

3. Activate the Conda environment

After the environment is created, activate it using:

conda activate nanopore-qc

This ensures that the correct versions of Snakemake, NanoPlot, and Python libraries are used.

4. Make sure the input FASTQ file is available

Place the FASTQ file in the expected location used by the workflow.

Example:

barcode77.fastq

If the file path is different, it should be updated in the workflow accordingly.

5. Run the Snakemake workflow

Execute the pipeline with:

snakemake --cores 4

This command tells Snakemake to run the workflow using 4 CPU cores.

If needed, the number of cores can be changed.

Example:

snakemake --cores 1

for a simpler run on a smaller machine.

6. Check the generated outputs

After the workflow completes, the main outputs should be available in the following locations:

QC results
results/qc/
Per-read statistics
results/read_stats.csv
Summary statistics
results/summary_stats.txt
Visualization outputs
figures/
Main Output Files
results/read_stats.csv

This file contains per-read statistics calculated from the FASTQ file.

Columns include:

Read_ID

Read_Length

GC_Content

Mean_Quality

results/summary_stats.txt

This file contains summary statistics for:

GC content

read length

mean quality score

It provides a quick numerical overview of the dataset.

figures/gc_distribution.png

This figure shows the distribution of GC content across reads.

figures/read_length_distribution.png

This figure shows the distribution of read lengths.

figures/quality_distribution.png

This figure shows the distribution of mean read quality scores.

results/qc/

This directory contains the outputs generated by NanoPlot.
These files provide additional quality control information for the long-read sequencing dataset.

Interpretation of Results

The plots and summary statistics generated by this pipeline help evaluate whether the sequencing dataset is suitable for downstream analysis.

For example:

GC content distribution helps identify unusual base composition patterns.

Read length distribution shows whether the dataset contains the long reads expected from Nanopore sequencing.

Mean quality score distribution helps assess overall sequencing quality.

Together, these outputs provide a clear overview of read quality before proceeding to alignment or other downstream steps.

Reproducibility

This workflow was designed to be reproducible.

Reproducibility is supported by:

use of Snakemake to define the workflow

use of environment.yml to define software dependencies

separation of scripts, results, and figures into organized folders

generation of outputs directly from the input data through the pipeline

Notes

The FASTQ input file may be too large to upload directly to GitHub.

In such cases, the pipeline can still be reproduced locally as long as the input file is available.

The repository mainly focuses on the workflow, scripts, outputs, and documentation.

Author

This repository was prepared as part of a mini bioinformatics pipeline and reporting case study.
