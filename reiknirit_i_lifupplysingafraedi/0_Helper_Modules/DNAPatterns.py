# coding=utf-8
from collections import defaultdict
import numpy as np

class DNA:
    def __init__(self, dnaString):
        self.dna = dnaString
        self.length = len(self.dna)
    
    def getString(self):
        return self.dna

    def text(self, i, k):
        return self.dna[i:i+k]

    def count(self, pattern):
        pattLen = len(pattern)
        count = 0
        for i in range(self.dna[:self.length-pattLen]):
            if self.text(i,pattLen) == pattern:
                count = count + 1
        return count

    def minimizeSkew(self, start, end):
        genome = self.dna[start:end]
        currentSkew = 0
        minSkews = [[1, -1]]
        
        for i, c in enumerate(genome):
            if c == 'C':
                currentSkew = currentSkew - 1
            elif c == 'G':
                currentSkew = currentSkew + 1
            if currentSkew == minSkews[0][0]:
                # i + 1 because http://rosalind.info/problems/ba1f/?class=431
                # does not expect indices, but rather the length of the substring
                minSkews.append([currentSkew, i + 1])
            elif currentSkew < minSkews[0][0]:
                minSkews = [[currentSkew, i + 1]]
        return minSkews

    def reverseCompliment(self):
        result = [] 
        for c in self.dna:
            if c == 'A':
               result.append('T')
            elif c == 'T':
               result.append('A')
            elif c == 'C':
               result.append('G')
            elif c == 'G':
               result.append('C')
        result.reverse()
        return ''.join(result)

    def hammingDistance(self, start, compareDNA):
        count = 0
        for i, c in enumerate(compareDNA):
            if c != self.dna[start + i]:
                count = count + 1
        
        return count

    def minHammingDistancePositions(self, compareDNA, maxDistance):
        compateLength = len(compareDNA)
        indices = []
        for i in range(self.length - compateLength + 1):
            distance = self.hammingDistance(i, compareDNA)
            if distance <= maxDistance:
                indices.append(i)
        return indices

    def kMersWithMinHammingDistance(self, k, d):
        allCounts = []
        for i in range(self.length):
            kMer = self.dna[i:i+k]
            count = 0
            for j in range(self.length):
                if self.hammingDistance(j,kMer) <= d:
                    count = count + 1
            allCounts.append(count)

        print allCounts
        return True

