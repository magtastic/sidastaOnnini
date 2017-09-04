# coding=utf-8
import sys
sys.path.insert(0, '/Users/magtastic/Documents/Skoli/ar4/sidastaOnnini/reiknirit_i_lifupplysingafraedi/0_Helper_Modules')
from DNAPatterns import DNA

PATTERN = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
DNA_STRING = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

myDNAString = DNA(DNA_STRING)
indexes = []
for i, c in enumerate(myDNAString.getString()):
    if myDNAString.text(i, len(PATTERN)) == PATTERN:
        indexes.append(i)

print indexes