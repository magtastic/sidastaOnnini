# coding=utf-8
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path[:dir_path.rfind('/')] + '/0_Helper_Modules'
sys.path.insert(0, dir_path)
from DNAPatterns import DNA

DNA_STRING = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
K_AND_D = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

K = int(K_AND_D.split()[0])
D = int(K_AND_D.split()[1])
myDNA = DNA(DNA_STRING)
# kMers = myDNA.kMersWithMinHammingDistance(K,D)
# print ' '.join(kMers)

allPossiblekMers = myDNA.getAllPossibleKmers(K)
allCounts = []
for kMer in allPossiblekMers:
    allCounts.append(myDNA.howOftenkMerAppearsWithMinHammingDistance(kMer, D))

maxCount = 0
maxKMers = []
kMersCounts = dict(zip(allPossiblekMers, allCounts))
for kMer in kMersCounts:
    print maxCount
    if kMersCounts[kMer] > maxCount:
        maxCount = kMersCounts[kMer] 
        maxKMers = [ kMer ]
    elif kMersCounts[kMer] == maxCount:
        maxKMers.append(kMer)

print ' '.join(maxKMers)