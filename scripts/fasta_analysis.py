def read_fasta(filename):
    seq = ""
    with open(filename) as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
    return seq

sequence = read_fasta("data/sequence.fasta")
print(sequence)
