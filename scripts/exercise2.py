#!/bin/python

##Q1; Calculate the percent GC and AT content a string called trna.

trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'

###looking for the length of trna
print(len(trna))

###counting the numbers of As, Ts, Gs and Cs independently
A_content=trna.count('A')
C_content=trna.count('C')
G_content=trna.count('G')
T_content=trna.count('T')

###calculating percent GC and percent AT content
AT_content=((A_content + T_content)/len(trna))*100
GC_content=((G_content + C_content)/len(trna))*100
print(AT_content) # Ass messages to make the print out informative -1
print(GC_content)
print("The trna has a GC content of %.3f and AT content of %.3f The length of the DNA is %d." % (GC_content, AT_content, len(trna)))

