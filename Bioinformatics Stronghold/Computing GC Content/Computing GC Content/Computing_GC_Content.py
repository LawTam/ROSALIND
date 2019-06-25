def main():
    # Manage input file
    input = open(r"","r");

    input.close();


# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
#           Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; 
#           please see the note on absolute error below.
def highestGC(dict):
    maximum = max(dict.values());
    result = filter(lambda x:x[1] == maximum,dic.items());  # returns the set of keys that have the maximum value



# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: Dictionary of the format: for all XXXX, { Rosalind_XXXX (FASTA) : "GC-content percentage" }
def DNA_to_GC(file):
    # Declare variables
    line_index = 0;
    GC_dict = {};
    FASTA = -1;

    for line in file:
        # Iterate line index
        line_index += 1;

        # Reset char index and find length of line
        char_index = 0;
        line_len = len(line);

        # FIRST:: Check IF the new line dictates a new key
        if line[0] == ">":
           # Generate new key "Rosalind_XXXX" for the following DNA string
           FASTA = str(line[1:]);   # FUN FACT: FASTA is a common format for labeling DNA strings
                                       #    AND we are decoding FASTA format in this script
           GC_dict[FASTA] = 0;      # Declare it in the dictionary
           
           # Declare & reset the gc_content calculation values for the new key
           num_n = 0;       # total number of nucleotides in the DNA string
           num_GC = 0;      # number of Guanine and Cytosine in the DNA string
           gc_content = 0;  # gc_content = num_GC / num_n

        # SECOND:: If line does not dictate a new key, calculate gc_content
        else:      
            # Calculate the gc_content calculation values for the DNA string until one of the following conditions hold
            #   Condition 1: end of line and next line is a key
            #   Condition 2: end of line and next line is EOF, aka the empty string ""
            if FASTA != -1:
                for n in line:
                    # 1. Iterate char index
                    char_index += 1;

                    # 2. Calculate the gc_content calculation values for the DNA string
                    if n is "A" or "T":
                        num_n += 1;
                    elif n is "G" or "C":
                        num_GC += 1;

                    # 3. Check if end of line
                    #   IF end of line, check next line 
                    #   IF next line signals end of the DNA string
                    #       1. Calculate GC Content
                    #       2. Update GC_dict with the key's corresponding GC content
                    if char_index is line_len:
                        if file[line_index + 1][0] is "" or ">":
                            gc_content = num_GC / num_n;
                            GC_dict[FASTA] = gc_content;
            else:
                # FASTA == -1
                print("order of input file is incorrect");

    return GC_dict;

# Manually call main() on the file load
if __name__ == "__main__":
     main();