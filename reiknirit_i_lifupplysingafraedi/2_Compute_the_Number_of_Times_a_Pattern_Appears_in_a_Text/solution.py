# coding=utf-8
import sys

DNA = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
PATTERN = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

def patternCount(dna, pattern):
    patternLenght = len(pattern)
    count = 0
    for i, _ in enumerate(dna):
        if dna[i:i + patternLenght] == pattern:
            count = count + 1
    return count

print patternCount(DNA, PATTERN)
