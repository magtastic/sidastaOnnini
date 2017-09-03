# coding=utf-8
import sys

DNA = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
PATTERN_LENGTH = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

def mostFrequentPattern(dna, patternLength):
    countObject = {}
    maxPattern = [[0, '']]
    for i, c in enumerate(dna):
        pattern = dna[i:i+patternLength]
        try:
            countObject[pattern] = countObject[pattern] + 1
            if countObject[pattern] == maxPattern[0][0]:
              maxPattern.append([countObject[pattern], pattern])
            elif countObject[pattern] > maxPattern[0][0]:
              maxPattern = [[countObject[pattern], pattern]]
        except:
            countObject[pattern] = 1
    print countObject
    print '=----------------='
    print maxPattern
    print '=----------------='
    return maxPattern

mostFrequentPattern(DNA, int(PATTERN_LENGTH))
