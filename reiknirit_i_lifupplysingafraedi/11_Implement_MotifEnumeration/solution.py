# coding=utf-8
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path[:dir_path.rfind('/')] + '/0_Helper_Modules'
sys.path.insert(0, dir_path)
from DNAPatterns import DNA

K_AND_D = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
DNAStrings = []
while True:
    DNA_STRING = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
    if len(DNA_STRING.split()) == 1:
        DNAStrings.append(DNA(DNA_STRING))
    else:
        break

K = int(K_AND_D.split()[0])
D = int(K_AND_D.split()[1])

myDNA = DNA('')

allPossibleDNAStrings = myDNA.getAllPossibleKmers(K)
kMersExistInAll = []
for kMer in allPossibleDNAStrings:
    wasBroken = False
    for dna in DNAStrings:
        doesExist = dna.kMerExistsWithMaxHammingDistance(kMer, D)
        if not doesExist:
            wasBroken = True
            break

    if not wasBroken:
        kMersExistInAll.append(kMer)

print '----GOT----'
print ' '.join(kMersExistInAll)


