from Bio import SeqIO

fastq_file = "barcode77.fastq"
output_file = "barcode77_high_quality.fastq"

with open(output_file, "w") as out_handle:
    for record in SeqIO.parse(fastq_file, "fastq"):
        if min(record.letter_annotations['phred_quality']) >= 20:
            SeqIO.write(record, out_handle, "fastq")

print(f"Filtered reads saved to {output_file}")
