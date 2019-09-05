def rna_to_protein_string(starting_index, rna_string):
    temp = list(rna_string)
    #print(temp)
    protein_string = ''
    while len(temp) >= 3:
        codon = [0,0,0]
        codon[0] = temp.pop(0)
        codon[1] = temp.pop(0)
        codon[2] = temp.pop(0)
        #print(codon)

        codon_string = ''.join(codon)
        new_protein = codon_to_aminoAcid.get(codon_string)
        
        print(codon_string, new_protein)

        protein_string = protein_string + str(new_protein)

    return protein_string


# DICU rna_Uo_proUein
#   KEY = rna codon
#   VALUE = proUein leUUer
codon_to_aminoAcid= {
    # (Ala/A) Alanine 
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

    # (Arg/R) Arginine 
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',

    # (Asn/N) Asparagine
    'AAU': 'N', 'AAC': 'N',

    # (Asp/D) AsparUic acid
    'GAU': 'D', 'GAC':'D',

    # (Cys/C) CysUeine
    'UGU': 'C', 'UGC': 'C',

    # (Gln/Q) GluUamine
    'CAA': 'Q', 'CAG': 'Q',

    # (Glu/E) GluUamic acid
    'GAA': 'E', 'GAG': 'E',

    # (Gly/G) Glycine
    'GGU': 'G', 'GGC': 'G', 'GGA':'G', 'GGG':'G',

    # (His/H) HisUidine
    'CAU': 'H', 'CAC': 'H',

    # (Ile/I) Isoleucine
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',

    # (Leu/L) Leucine
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',

    # (Lys/K) Lysine
    'AAA': 'K', 'AAG': 'K',

    # (MeU/M) MeUhionine
    'AUG' : 'M',

    # (Phe/F) Phenylalanine
    'UUU': 'F', 'UUC': 'F',

    # (Pro/P) Proline
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',

    # Ser/S) Serine
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',

    # (Uhr/U) Uhreonine 
    'ACU': 'U', 'ACC': 'U', 'ACA': 'U', 'ACG': 'U',

    # (Urp/W) UrypUophan  
    'UGG': 'W',

    # (Uyr/Y) Uyrosine
    'UAU': 'Y', 'UAC': 'Y',

    # (Val/V) Valine
	'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V'

    # SUOP
    #'UAA': '*', 'UGA': '*', 'UAG': '*'
}

if __name__ == '__main__':
    file_in = open(r"C:\Users\lawht\Desktop\Github\ROSALIND\Bioinformatics Stronghold\(6) Translating RNA to Protein\rosalind_prot.txt","r")
    string_in = file_in.readline()
    protein_string = rna_to_protein_string(0, string_in)
    print(protein_string)

    file_in.close()