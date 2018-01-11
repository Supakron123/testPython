def to_rna(dna_strand):
    dna = []
    dna_strand = list(dna_strand)
    print(f'DNA : {dna_strand}')
    for i in dna_strand:
        if i in 'GCTA':
            if i == 'G':
                dna.append('C')
            elif i == 'C':
                dna.append('G')
            elif i == 'T':
                dna.append('A')
            else:
                dna.append('U')
        else:
            raise ValueError
    return ''.join(dna) 

    