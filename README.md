 Bioinformatics Pipeline for Long-Read Sequencing Quality Control

## Project Description

This project implements a reproducible bioinformatics pipeline designed to analyze long-read sequencing data.  
The main goal of the pipeline is to perform quality control (QC), calculate key statistics for each sequencing read, and generate visualizations that summarize the characteristics of the dataset before downstream analysis.

The workflow was implemented using **Snakemake** and custom **Python scripts**.

---

## Objectives

The pipeline performs the following tasks:

1. Run a quality control tool specifically designed for long-read sequencing data.
2. Calculate important statistics for each read in the FASTQ file:
   - GC content percentage
   - Read length
   - Mean read quality score
3. Save the calculated statistics in a structured format.
4. Generate visualizations showing the distribution of the calculated metrics.

---

## Quality Control Tool

This pipeline integrates **NanoPlot**, which is a quality control tool designed for long-read sequencing technologies such as Oxford Nanopore.

NanoPlot generates several QC outputs including:

- read length distributions
- quality score distributions
- yield plots
- interactive HTML reports

These outputs help assess whether the sequencing data is suitable for downstream analysis.

---

## Custom Read Statistics Analysis

A custom Python script analyzes each read in the FASTQ file and calculates the following metrics:

- GC Content
- Read Length
- Mean Read Quality Score

The results are stored in a CSV file:
