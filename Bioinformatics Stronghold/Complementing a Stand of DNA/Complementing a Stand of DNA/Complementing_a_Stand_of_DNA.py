def main():
    # Manage input file
    input = open(r"C:\Users\lawht\Desktop\Github\ROSALIND\Bioinformatics Stronghold\Complementing a Stand of DNA\Complementing a Stand of DNA\rosalind_revc.txt","r");
    DNA_string = input.readline();  # take first line of input file for counting

    # Take in input file of DNA string and print out its reverse complement
    print(reverse_complement(DNA_string));

    input.close();

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.
def reverse_complement(s):
    sc = "";
    for n in reversed(s):
        if n == "A":
            sc = sc + "T";
        elif n == "T":
            sc = sc + "A";
        elif n == "C":
            sc = sc + "G";
        elif n == "G":
            sc = sc + "C";
        else:
            continue

    return sc;

# Manually call main() on the file load
if __name__ == "__main__":
     main();