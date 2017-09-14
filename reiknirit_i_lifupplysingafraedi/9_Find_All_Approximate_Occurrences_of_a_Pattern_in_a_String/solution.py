# coding=utf-8
import sys
sys.path.insert(0, '/Users/magtastic/Documents/Skoli/ar4/sidastaOnnini/reiknirit_i_lifupplysingafraedi/0_Helper_Modules')
from DNAPatterns import DNA

PATTERN = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
DNA_STRING = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
MAX_DISTANCE = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
EXPECT = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

myDNA = DNA(DNA_STRING)
indices = myDNA.minHammingDistancePositions(PATTERN, int(MAX_DISTANCE))
print ' '.join(str(x) for x in indices)
print EXPECT == ' '.join(str(x) for x in indices)
print EXPECT