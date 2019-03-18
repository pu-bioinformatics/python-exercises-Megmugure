#!/bin/python

##Q1; Write a function that calculates the GC content of a DNA sequence.

def percentageGC(trna):
    """This function calculates the %GC content of a DNA sequence"""
    trna = trna.upper()
    G_count=trna.count('G')
    C_count=trna.count('C')
    GC_content = ((G_count+ C_count)/len(trna))*100
    return GC_content

###Using the function to calculate the GC content of trna.
trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'

print(percentageGC(trna))

##Q2; Write a function that checks if a DNA sequence is valid or not by checking all the bases.
def dnafunc(dna):
    """This function checks the validity of a DNA sequence"""
    bases = 'ATGC'
    for base in dna:
        if base not in bases:
            return ("This is not a valid DNA")
    else:
        return ("This is a valid DNA")

###Using the new function to cofirm validity of several DNA sequences.
mydna = "CAGTGATGATGACGAT"
yourdna = "ACGATCGAGACGTAGTA"
testdna = "ATFRACGATTGHAHYAK"

print(dnafunc(mydna))

print(dnafunc(yourdna))

print(dnafunc(testdna))
