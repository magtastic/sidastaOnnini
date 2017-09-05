# coding=utf-8
from collections import defaultdict
import sys
sys.path.insert(0, '/Users/magtastic/Documents/Skoli/ar4/sidastaOnnini/reiknirit_i_lifupplysingafraedi/0_Helper_Modules')
from DNAPatterns import DNA

DNA_STRING = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
SOME_NUMBERS = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

SOME_NUMBERS = SOME_NUMBERS.split(' ')
k = int(SOME_NUMBERS[0])
L = int(SOME_NUMBERS[1])
t = int(SOME_NUMBERS[2])

myDNA = DNA(DNA_STRING)

indexes = defaultdict(list)
correctPatterns = []

for i in range( (len(myDNA.getString()) - k) + 1):
    pattern = myDNA.text(i, k)
    indexes[pattern].append(i)
    indexCount = len(indexes[pattern])
    if indexCount == t:
        if indexes[pattern][-1] - indexes[pattern][-t] <= L:
            if pattern not in correctPatterns:
                correctPatterns.append(pattern)


print correctPatterns

