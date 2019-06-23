def main():
    # Declare nucleotide variables [Adenine, Cytosine, Guanine, Thymine]
    A = 0;
    C = 0;
    G = 0;
    T = 0;

    # Manage input file
    input = open(r"C:\Users\lawht\Desktop\Github\ROSALIND\Bioinformatics Stronghold\(1) Counting DNA Nucleotides\Counting DNA Nucleotides\rosalind_dna.txt","r");
    DNA_string = input.readline();  # take first line of input file for counting

    # Take in input file of DNA string and count the number of each nucleotide
    count_nucleotides(DNA_string, A, C, G, T);

    input.close();


# INPUT:
#   s = DNA string
#   a,c,g,t = stored number of counted a,c,g,t
#
# OUTPUT:
#   Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
def count_nucleotides(s, a, c, g, t):
    for n in s:
        if n == 'A':
            a+=1;
        elif n == 'C':
            c+=1;
        elif n == 'G':
            g+=1;
        elif n == 'T':
            t+=1;
        else:
            continue;
    print(a,c,g,t);
    return 

# It is required in python to call manually main()
if __name__ == "__main__":
     main();