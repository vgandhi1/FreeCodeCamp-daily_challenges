"""
Complementary DNA
Given a string representing a DNA sequence, return its complementary strand using the following rules:

DNA consists of the letters "A", "C", "G", and "T".
The letters "A" and "T" complement each other.
The letters "C" and "G" complement each other.
For example, given "ACGT", return "TGCA".
"""
def complementary_dna(strand):

    #efficiency slower O(n) for list 
    #DNA_letters = ['A','C','G','T']
    
    #efficiency slower O(1) for dictionary & set 
    DNA_letters = {'A','C','G','T'}
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


# Constants built once
# for loop - O(n) slower effficiency
_DNA_LETTERS = {'A', 'C', 'G', 'T'}
_COMP_MAP = str.maketrans("ACGT", "TGCA")

def complementary_dna(strand: str) -> str:
    s = strand.upper()
    # Fast validity check
    if set(s) - _DNA_LETTERS:
        raise ValueError("Incorrect DNA strand")
    return s.translate(_COMP_MAP)
        

# Examples
print(complementary_dna("ATGCGTACGTTAGC"))  # TGCA
