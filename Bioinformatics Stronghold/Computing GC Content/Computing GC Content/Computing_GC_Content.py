def main():
    # Manage input file
    input = open(r"","r");

    input.close();

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
#           Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; 
#           please see the note on absolute error below.
def highestGC(dict):


# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: Dictionary of the format: for all XXXX, { Rosalind_XXXX (FASTA) : "GC-content percentage" }
def DNA_to_GC(file):
    GC_dict = {};
    FASTA = -1;
    gc_content = 0;
    for line in file:
        # Check if line dictates a new key
        if line[0] == ">":
           # Generate new key "Rosalind_XXXX" for the following DNA string
           FASTA = str(line[1:]);
           GC_dict[FASTA] = 0;  # Declare it in the dictionary
           gc_content = 0;  # Declare & reset the gc_content calculation for the new key
        
        else:      
            # Calculate the GC Content for the DNA string until one of the following conditions hold
            #   Condition 1: end of line and next line is a key
            #   Condition 2: end of line and next line is EOF, aka the empty string ""
            if FASTA != -1:
                

            else:
                print("order of input file is incorrect");

            


# Manually call main() on the file load
if __name__ == "__main__":
     main();