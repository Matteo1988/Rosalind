# solution inspired by http://saradoesbioinformatics.blogspot.com/2016/07/finding-shared-motif.html
from Bio import SeqIO

out = open("soluzione.txt","w")

sequences = []

for seq in SeqIO.parse("prova.fasta", "fasta"):
    sequences.append(str(seq.seq))


sorted_seq = sorted(sequences, key=len)
shortest = sorted_seq[0]
other_sequences = sorted_seq[1:]
longest_substring = ""

for i in range(len(shortest)):
    for j in range(i, len(shortest)):
        possible_substring = shortest[i:j+1]
        match_found = False
        for sequence_compared in other_sequences:
            if possible_substring in sequence_compared:
                match_found = True
            else:
                match_found = False
                break

        if match_found and len(possible_substring) > len(longest_substring):
            longest_substring = possible_substring

print("soluzione: "+longest_substring)

out.write(longest_substring)



########FIND LONGEST SUBSEQUENCE BETWEEN TWO SEQUENCE

# for seq1 in sequences:
#
    # for seq2 in sequences:
        # if seq1 != seq2:
            # seqMa = SequenceMatcher(None,seq1,seq2)
            # match = seqMa.find_longest_match(0, len(seq1), 0, len(seq2))
            # if (match.size != 0):
                # sequence = seq1[match.a: match.a + match.size]
                # if sequence not in common_seq:
                    # common_seq.append(sequence)
#
# longest_seq = []
#
# longest = 0
#
# for seq in common_seq:
    # l = len(seq)
    # if l > longest:
        # longest = l
        # longest_seq = [seq]
    # elif l == longest:
        # longest_seq.append(seq)
#
