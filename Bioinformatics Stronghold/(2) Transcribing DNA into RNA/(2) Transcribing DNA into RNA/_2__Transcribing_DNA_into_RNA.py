def main():
    # Manage input file
    input = open(r"C:\Users\lawht\Desktop\Github\ROSALIND\Bioinformatics Stronghold\(2) Transcribing DNA into RNA\(2) Transcribing DNA into RNA\rosalind_rna.txt","r");
    DNA_string = input.readline();  # take first line of input file for counting

    # Take in input file of DNA string and print out its corresponding RNA sequence
    print(DNA_to_RNA(DNA_string));

    input.close();

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.
def DNA_to_RNA(s):
    rna = "";
    for n in s:
        if n == "T":
            rna = rna + "U";
        else:
            rna = rna + n;

    return rna;

# Manually call main() on the file load
if __name__ == "__main__":
     main();