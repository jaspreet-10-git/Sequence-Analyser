import pandas as pd
import numpy as np
import Bio

from Bio.Seq import Seq
dna_seq=Seq(input("Please enter the DNA sequence:").strip().upper())
if len(dna_seq)%3 == 0:
    rna_seq=dna_seq.transcribe()
    protein=rna_seq.translate()
    print("The complementary sequence for the given sequence is:", dna_seq.complement())
    print("The reverse complement for the given sequence is:", dna_seq.reverse_complement())
    print("The RNA transcript for the given sequence is:", dna_seq.transcribe())
    print("The protein formed by the translation of the given sequence is:",protein)

#import Seq class from Bio.Seq module to display DNA sequences etc. in string format
from Bio.Seq import Seq
#import SeqRecord class Bio.Record module to display the records of the sequence 
from Bio.SeqRecord import SeqRecord
seq_record=SeqRecord(Seq("ATGCAGTGA"), id='NC_001234',description='Hypothetical protein from E.coli')
seq_record.annotations['gene']='geneX'
print(f"Sequence ID: {seq_record.id}")
print(f"Sequence Description: {seq_record.description}")
print(f"Sequence Gene (from annotations): {seq_record.annotations['gene']}")

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
seq_record_2=SeqRecord(Seq("ATGAGACTGAACTATA"),id= 'NC_00567',description='Hypothetical protein 2')
seq_record_2.annotations['gene_2']='geneX_2'
print(f"Sequence ID given: {seq_record_2.id}")
print(f"Sequence description: {seq_record_2.description}")
print(f"Sequence gene_2(from annotations): {seq_record_2.annotations['gene_2']}")

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
seq_record_3=SeqRecord(Seq("ATGGACGCAAGT"),id='NC_00789',description='Hypothetical protein 3')
seq_record_3.annotations['gene_3']='geneX_3'
print(f"Sequence ID :{seq_record_3.id}")
print(f"Sequence description: {seq_record_3.description}")
print(f"Sequence gene_3(from annotations): {seq_record_3.annotations['gene_3']}")

#import SeqIO from Bio module to display a FASTA sequence presaved in your system
from Bio import SeqIO
for record in SeqIO.parse("/Users/jaspreetmarwaha/Desktop/Computational Biology/sequence-2.fasta","fasta"):
    print(f"ID: {record.id}")
    print(f"Sequence: {record.seq}")
    seq_record_2=SeqIO.read("/Users/jaspreetmarwaha/Desktop/Computational Biology/sequence-2.fasta","fasta")
print(seq_record_2)

from Bio import SeqIO
for record_2 in SeqIO.parse("/Users/jaspreetmarwaha/Desktop/Computational Biology/sequence-3.fasta","fasta"):
    print(f"ID: {record_2.id}")
    print(f"Sequence:{record_2.seq}")
seq_record_3=("/Users/jaspreetmarwaha/Desktop/Computational Biology/sequence-3.fasta","fasta")
print(seq_record_3)

from Bio import SeqIO
for record_3 in SeqIO.parse("/Users/jaspreetmarwaha/Desktop/Computational Biology/sequence-3.fasta","fasta"):
    print(f"ID: {record_3.id}")
    print(f"Sequence:{record.seq}")
seq_record_3=SeqIO.read("/Users/jaspreetmarwaha/Desktop/Computational Biology/sequence-3.fasta","fasta")
print(seq_record_3)

from Bio import Entrez
Entrez.email='jazzymm10@gmail.com'
handle=Entrez.esearch(db="pubmed", term="Biopython", retmax="10")
record=Entrez.read(handle)
handle.close()
print("PubMed IDs:",record["IdList"])
handle=Entrez.efetch(db="nucleotide",id='LT934502',rettype='gb',retmode='text')
gen_bank=handle.read()
handle.close()
print(gen_bank[:500])

from Bio import Entrez
Entrez.email='jazzymm10@gmail.com'
handle_2=Entrez.esearch(db='pmc',term='human genetics',retmax='5')
record_2=Entrez.read(handle_2)
handle_2.close()
print('Sequence IDs:',record_2['IdList'])
handle_2=Entrez.efetch(db='pmc',id='PMC9897628',rettype='gb',retmode='text')
gen_bank_2=handle_2.read()
handle_2.close()
print(gen_bank_2[:500])






    


