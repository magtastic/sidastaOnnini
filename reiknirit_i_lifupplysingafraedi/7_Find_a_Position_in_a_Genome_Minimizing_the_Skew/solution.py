# coding=utf-8
import sys
sys.path.insert(0, '/Users/magtastic/Documents/Skoli/ar4/sidastaOnnini/reiknirit_i_lifupplysingafraedi/0_Helper_Modules')
from DNAPatterns import DNA

DNA_STRING = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
myDNA = DNA(DNA_STRING)
minSkews = myDNA.minimizeSkew(0, len(DNA_STRING))

lengths = []
for i in minSkews:
    lengths.append(str(i[1]))

print ' '.join(lengths)
