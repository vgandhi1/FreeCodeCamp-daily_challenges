"""
Complementary DNA
Given a string representing a DNA sequence, return its complementary strand using the following rules:

DNA consists of the letters "A", "C", "G", and "T".
The letters "A" and "T" complement each other.
The letters "C" and "G" complement each other.
For example, given "ACGT", return "TGCA".
"""
def complementary_dna(strand):

    DNA_letters = ['A','C','G','T']
    strand = strand.upper()
  

    check_DNA_ltters = all(letter in DNA_letters for letter in strand.upper())
    if check_DNA_ltters:
        # Apply the translation map
        complement_map = str.maketrans("ACGT", "TGCA")
        final_strand = strand.translate(complement_map)
        return final_strand
    
    else:
        return "Incorrect DNA strand"

print(complementary_dna("ACGT")) 

"""
1. complementary_dna("ACGT") should return "TGCA".
2. complementary_dna("ATGCGTACGTTAGC") should return "TACGCATGCAATCG".
3. complementary_dna("GGCTTACGATCGAAG") should return "CCGAATGCTAGCTTC".
4. complementary_dna("GATCTAGCTAGGCTAGCTAG") should return "CTAGATCGATCCGATCGATC".
"""
