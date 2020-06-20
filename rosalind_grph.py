#first save rosalind_grph.txt as prova.fasta

from Bio import SeqIO

sequenze={}

k = 3 # number of nucleotides that overlaps

for seq in SeqIO.parse("prova.fasta", "fasta"):

    sequenze[seq.id] = str(seq.seq)

for key1,value1 in sequenze.items():
    for key2, value2 in sequenze.items():
        if key1 != key2 and value1[0:k] == value2[-k:]:
            print(key2, key1)
