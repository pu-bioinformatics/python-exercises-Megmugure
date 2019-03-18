#!/bin/python

## Q1; Using strings, lists, tuples and dictionaries concepts to find the reverse complement of AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA.

DNA="AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"

###replace each nucleotide with the complimentary base but in lower case and print the result.
DNA=DNA.replace('T','a')
DNA=DNA.replace('A','t')
DNA=DNA.replace('G','c')
DNA=DNA.replace('C','g')
print(DNA)

###reverse the string of DNA to get the reverse complement and name it RC.
RC=DNA[::-1]
print(RC)

###convert the letters in the reverse complement above to upper case.
print(RC.upper())

