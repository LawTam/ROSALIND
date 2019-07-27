def main():
    input = open(r"C:\Users\lawht\Desktop\Github\ROSALIND\Bioinformatics Stronghold\(5) Intro to Mandelian Inheritance\rosalind_iprb.txt","r")
    string_in = input.readline()
    probability = dominant_allele_percentage(string_in)
    print(probability)

    input.close()


def dominant_allele_percentage(population_str):
    population = [int(n) for n in population_str.split()]

    print(population)
    # population[0] = # homozygous dominant
    # population[1] = # heterozygous
    # population[2] = # homozygous recessive

    # Allocate gene pool values
    num_dominant_alleles = 0
    num_recessive_alleles = 0
    num_total_alleles = 0

    num_dominant_alleles += 2 * population[0]
    num_dominant_alleles += population[1]
    num_recessive_alleles += population[1]
    num_recessive_alleles += 2 * population[2]

    num_total_alleles = num_dominant_alleles + num_recessive_alleles

    print("dom", num_dominant_alleles)
    print("recessive", num_recessive_alleles)
    print("total", num_total_alleles)

    # Find: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
    #   (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
    #      
    #   There are 4 cases for the offspring type:
    #           a. FIRST ALLELE: dominant, SECOND ALLELE: dominant
    #           b. FIRST ALLELE: dominant, SECOND ALLELE: recessive
    #           c. FIRST ALLELE: recessive, SECOND ALLELE: dominant
    #           d. FIRST ALLELE: recessive, SECOND ALLELE: recessive 
    #           (WE DO NOT CARE ABOUT d. BECAUSE THIS OFFSPRING IS NOT DISPLAYING DOMINANT PHENOTYPE)

    # Therefore, there can only be two choices for the first and second allele - dominant or recessive. 
    #   Range() value is 2 => Dominant = 0, Recessive = 1
    for first_allele in range(2):
        for second_allele in range(2):
            
            # FIRST ALLELE = dominant
            if first_allele is 0:
                # SECOND ALLELE = dominant
                if second_allele is 0:
                    chance_00 = (num_dominant_alleles/num_total_alleles) * ((num_dominant_alleles-1)/(num_total_alleles-1))
                    
                # SECOND ALLELE = recessive
                if second_allele is 1:
                    chance_01 = (num_dominant_alleles/num_total_alleles) * (num_recessive_alleles/(num_total_alleles-1))
                    
            # FIRST ALLELE = recessive
            if first_allele is 1:
                # SECOND ALLELE = dominant
                if second_allele is 0:
                    chance_10 = (num_recessive_alleles/num_total_alleles) * (num_dominant_alleles/(num_total_alleles-1))
                    
                # SECOND ALLELE = recessive
                # if second_allele is 1:
                #     chance_11 = (num_recessive_alleles/num_total_alleles) + ((num_recessive_alleles-1)/(num_total_alleles-1)

    return chance_00 + chance_01 + chance_10
    

if __name__ == "__main__":
    main()
