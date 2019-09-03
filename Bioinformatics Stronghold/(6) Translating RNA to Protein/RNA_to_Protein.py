if __name == '__main__':
    file_in = open(r"","r")
    string_in = file_in.readline()
    protein_string = rna_to_protein_string(0, string_in)
    print(protein_string)

    file_in.close()

def rna_to_protein_string(starting_index, rna_string):
    

# DICT rna_to_protein
#   KEY = rna codon
#   VALUE = protein letter
rna_to_protein= {
    # (Ala/A) Alanine 
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

    # (Arg/R) Arginine 
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',

    # (Asn/N) Asparagine
    'AAT': 'N', 'AAC': 'N',

    # (Asp/D) Aspartic acid
    'GAT': 'D', 'GAC':'D',

    # (Cys/C) Cysteine
    'TGT': 'C', 'TGC': 'C',

    # (Gln/Q) Glutamine
    'CAA': 'Q', 'CAG': 'Q',

    # (Glu/E) Glutamic acid
    'GAA': 'E', 'GAG': 'E',

    # (Gly/G) Glycine
    'GGT': 'G', 'GGC': 'G', 'GGA':'G', 'GGG':'G',

    # (His/H) Histidine
    'CAT': 'H', 'CAC': 'H',

    # (Ile/I) Isoleucine
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',

    # (Leu/L) Leucine
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',

    # (Lys/K) Lysine
    'AAA': 'K', 'AAG': 'K',

    # (Met/M) Methionine
    'ATG' : 'M',

    # (Phe/F) Phenylalanine
    'TTT': 'F', 'TTC': 'F',

    # (Pro/P) Proline
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',



}