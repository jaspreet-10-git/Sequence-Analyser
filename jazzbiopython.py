import pandas as pd
import numpy as np
import Bio 

#basic sequence handling
from Bio.Seq import Seq
my_dna = Seq('ATGCCCTGT')
print(my_dna)
print(my_dna.complement())
print(my_dna.reverse_complement())
print(my_dna.transcribe())
my_rna= my_dna.transcribe()
print(my_rna.translate())


from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
record=SeqRecord(
    Seq('ATGCAGTGA'),
    id='NC_001234',
    description= 'Hypothetical protein from E.coli'
)
record.annotations['gene']='geneX'
print(f"Record Id :{record.id}")
print(f"Record Sequence:{record.seq}")
print(f"Record Description:{record.description}")
print(f"Gene (from annotations): {record.annotations['gene']}")

from Bio import SeqIO
for record in SeqIO.parse("/Users/jaspreetmarwaha/Desktop/Computational Biology/sequence.fasta","fasta"):
    print(f"ID :{record.id}")
    print(f"Sequence:{record.seq}")
seq_record=SeqIO.read("/Users/jaspreetmarwaha/Desktop/Computational Biology/sequence.fasta","fasta")
print(seq_record)

        

from Bio import Entrez

Entrez.email = "jazzymm10@gmail.com" # Always tell NCBI who you are

# Search for a term in PubMed
handle = Entrez.esearch(db="pubmed", term="Biopython", retmax="10")
record = Entrez.read(handle)
handle.close()
print("PubMed IDs:", record["IdList"])

# Fetch a GenBank record
handle = Entrez.efetch(db="nucleotide", id="NC_001477", rettype="gb", retmode="text")
genbank_record = handle.read()
handle.close()
print(genbank_record[:500]) # Print first 500 characters

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
result_handle=NCBIWWW.qblast("blastn","nt","ATGCGTACGT")
blast_record=NCBIXML.read(result_handle)

for alignment in blast_record.alignments:
    print(f"Alignemnt Title: {alignment.title}")
    for hsp in alignment.hsps:
        print(f"Alignment Score: {alignment.score}")
        print(f"Alignment E-value:{hsp.expect}")
result_handle.close()













