import operator

def main():
    # Manage input file
    rosalind_doc = open(r"C:\Users\lawht\Desktop\Github\ROSALIND\Bioinformatics Stronghold\(4) Computing GC Content\Computing GC Content\rosalind_gc.txt","r+")

    print("STAGE 1_____________________________________________")
    FASTA_dict = DNA_to_GC(rosalind_doc)    # create a corresponding dictionary for each FASTA
    
    print("STAGE 2_____________________________________________")
    print("-- Print the FASTA with the highest GC Content --\n")

    highestGC(FASTA_dict)   # print the FASTA with the highest GC Content

    rosalind_doc.close()

 
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
#           Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated 
#           please see the note on absolute error below.
def highestGC(dictionary):
    items = dictionary.items()
    maximum = max(dictionary.values())
    for key in items:
        if key[1] is maximum:
            print(key[0])
            print(key[1])


# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: Dictionary of the format: for all XXXX, { Rosalind_XXXX (FASTA) : "GC-content percentage" }
def DNA_to_GC(doc):
    read = doc.readlines()
    read.append("-\n")
    #print(read)
    doc_in = iter(read)     # read is a list, but a list is not a type iter
                            # so we manually set doc to an iter
    
    # Declare variables
    nucleotides = {"A", "T", "G", "C"}
    GC = {"G", "C"}
    string_enders = {"-", ">"}

    line_index = 0  # Which line we are on

    GC_dict = {} 
    FASTA = -1      # Name of FASTA key

    num_n = 0       # Total number of nucleotides in the DNA string
    num_GC = 0      # Number of Guanine and Cytosine in the DNA string
    gc_content = 0  # gc_content = num_GC / num_n

    for line in doc_in:
        #print(line)

        # Iterate line index
        line_index += 1

        # Reset char index and find length of line
        char_index = 0

        # FIRST:: Check IF the new line dictates a new key (aka end of previous key)
        if line[0] in string_enders:
            # If we have another gc_content ready, FINALIZE and store the value in GC_dict
            if(num_n > 0):
                #print("---------end of DNA string---------")
                gc_content = num_GC / num_n * 100
                GC_dict[FASTA] = gc_content    

            # Indicate start of new key
            #print(line[0], line_index)

            # If EOF, break -- do not create a new key
            if(line[0] is "-"):
                break 

            # Generate new key "Rosalind_XXXX" for the following DNA string
            FASTA = str(line[1:-1])   # FUN FACT: FASTA is a common format for labeling DNA strings
                                        #    AND we are decoding FASTA format in this script
            GC_dict[FASTA] = 0      # Declare it in the dictionary
            
            # Reset the gc_content calculation values for the new key
            num_n = 0       # total number of nucleotides in the DNA string
            num_GC = 0      # number of Guanine and Cytosine in the DNA string
            gc_content = 0  # gc_content = num_GC / num_n

        # SECOND:: If line does not dictate a new key, calculate gc_content
        else:      
            # Calculate the gc_content calculation values for the DNA string until one of the following conditions hold
            #   Condition 1: end of line and next line is a key
            #   Condition 2: end of line and next line is EOF, aka the empty string ""
            if FASTA != -1:
                for n in line:
                   # print(n)

                    # 1. Iterate variables
                    char_index += 1

                    # 2. Calculate the gc_content calculation values for the DNA string
                    if n in nucleotides:
                        num_n += 1
                        #print("num_n: ", num_n)
                        if n in GC:
                            num_GC += 1
                            #print("num_GC: ", num_GC)
                      
            else:
                # FASTA == -1
                print("order of input file is incorrect")
    
    print("-- {'FASTA key' : 'gc_content'} -- \n")
    print(GC_dict, "\n")

    return GC_dict


# Manually call main() on the file load
if __name__ == "__main__":
     main()