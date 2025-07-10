#Project 1: Sequence Analyser
from Bio.Seq import Seq #for representing biological sequences
from Bio import SeqIO #for reading and writing sequences files like FASTA, GenBank 
from Bio.SeqUtils import gc_fraction # utility function to calculate the GC content of the GC content 

#defining functions

#to prompt the user for input
def get_input():
    while True:
        choice=input("Do you want to enter a sequence directly (D) or provide a file path(F)?").strip().upper()
        if choice=='D':
            seq_str=input(("Enter the sequence:").strip())
            seq_type=input(("Is this a DNA (D) or a Protein (P) sequence?").strip().upper())

            if seq_type=='D':
                return Seq(seq_str),'DNA'
            elif seq_type=='P':
                return Seq(seq_str),'Protein'
            else :
                print("Please enter a valid sequence. Either DNA (D) or Protein(P).")
        
        elif choice=='F':
            
            file_path=input('Please enter the file path:').strip()
            try:
                record=SeqIO.read(file_path,'fasta')
                seq_type=input(f'Is the sequence in {file_path} a DNA sequence (D) or a Protein sequence (P)?').strip().upper()
                if seq_type=='D':
                   return record.seq ,'DNA'
                elif seq_type=='P':
                   return record.seq , 'Protein'
                else:
                 print("Please enter a valid sequence type, D for DNA and P for Protein")
            except FileNotFoundError:
                print(f"File not found at {file_path} .")
            except Exception as e:
                print('Error reading file :{e}')
        else:
            print("Invalid choice. Please enter D or F.")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")           
def analyse_seq(dna_seq:Seq):
    print(f"Orginal Sequence: {dna_seq}")
    print(f"The length of the given sequence is : {len(dna_seq)} bases")

    try:
        gc_content=gc_fraction(dna_seq)*100
        print(f"The GC content of the given DNA sequence is {gc_content: .2f}%")
        
    except Exception as e:
        print(f"Could not calculate GC content:{e}. Ensure it is a valid DNA/RNA sequence.")

    try:
        for frame in range(3):
            protein_seq= dna_seq[frame:].translate()
            print(f"Frame {frame+1} Translation : {protein_seq}")
        for frame in range(3):
            protein_seq_fwd=dna_seq[frame:].translate()
            print(f"Forward frame {frame+1}: {protein_seq_fwd}")
        
        rev_comp_dna_seq=dna_seq.reverse_complement()
        for frame in range(3):
            protein_comp_rev=rev_comp_dna_seq[frame:].translate()
            print(f"Reverse frame {frame+1}: {protein_comp_rev}")

    except Exception as e:
        print(f"Could not perform translation {e}. Please ensure that the sequence entered is valid.")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")           
if __name__== "__main__":
    print("Welcome to Sequence Analyser")
    sequence, seq_type=get_input()
    if sequence:
        if seq_type=="DNA":
            analyse_seq(sequence)
        elif seq_type=="Protein":
            print(f"Original sequence: {sequence}")
            print(f"Length of the original sequence: {len(sequence)} amino acids")
            print(f"Cannot perform GC content calculation  or a translation on a protein sequence")
        else :
            print("Unknown sequence")
    else:
        print("Invalid sequence")






            




