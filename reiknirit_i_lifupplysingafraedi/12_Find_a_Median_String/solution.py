# coding=utf-8
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path[:dir_path.rfind('/')] + '/0_Helper_Modules'
sys.path.insert(0, dir_path)
from DNAPatterns import DNA

K = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
K = int(K)
DNAStrings = []
for i in range(20):
    DNA_STRING = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
    if len(DNA_STRING) != 0:
        DNAStrings.append(DNA(DNA_STRING))
    else:
        break

allPossibleKMers = DNAStrings[0].getAllPossibleKmers(K)

kMersWithMinHammingDistance = []
minTotalHammingDistance = K * len(DNAStrings)
for kMer in allPossibleKMers:
    totalHammingDistance = 0
    for dnaString in DNAStrings:
        minHammingDistance = dnaString.minHammingDistance(kMer)
        totalHammingDistance = totalHammingDistance + minHammingDistance
    if totalHammingDistance < minTotalHammingDistance:
        minTotalHammingDistance = totalHammingDistance
        kMersWithMinHammingDistance = [ kMer ]
    elif totalHammingDistance == minTotalHammingDistance:
        kMersWithMinHammingDistance.append(kMer)

print kMersWithMinHammingDistance


#allSubStringOfAllDNA = dict()
#for dnaString in DNAStrings:
    #allSubStringOfAllDNA[dnaString.getString()] = dnaString.getAllKmersOfLength(K)

#for dnaString in allSubStringOfAllDNA:
    #for kMer in allSubStringOfAllDNA[dnaString]:

