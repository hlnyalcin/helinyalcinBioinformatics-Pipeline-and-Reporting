from Bio import SeqIO
import csv

fastq_file = "barcode77.fastq"

with open("read_stats.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Read_ID", "Read_Length", "GC_Content", "Mean_Quality"])

    for record in SeqIO.parse(fastq_file, "fastq"):
        seq = record.seq
        read_len = len(seq)
        gc_content = 100 * float(seq.count("G") + seq.count("C")) / read_len
        mean_quality = sum(record.letter_annotations["phred_quality"]) / read_len
        writer.writerow([record.id, read_len, gc_content, mean_quality])
