from Bio import SeqIO

fastq_file = "barcode77.fastq"

for record in SeqIO.parse(fastq_file, "fastq"):
    if min(record.letter_annotations['phred_quality']) >= 20:
        print(f"{record.id} passed quality filter")
