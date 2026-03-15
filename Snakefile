rule nanoplot:
    input:
        "barcode77.fastq"
    output:
        "qc/NanoPlot-report.html"
    shell:
        "NanoPlot --fastq barcode77.fastq --outdir qc"
