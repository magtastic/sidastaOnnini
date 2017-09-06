# coding=utf-8
import sys
sys.path.insert(0, '/Users/magtastic/Documents/Skoli/ar4/sidastaOnnini/reiknirit_i_lifupplysingafraedi/0_Helper_Modules')
from DNAPatterns import DNA

DNA_STRING_1 = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
DNA_STRING_2 = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
EXPECT = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

myDNA = DNA(DNA_STRING_1)
print myDNA.hammingDistance(DNA_STRING_2)