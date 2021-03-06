from __future__ import division
# coding=utf-8
from collections import defaultdict
from itertools import product
import numpy as np

class DNA:
    def __init__(self, dnaString):
        self.dna = dnaString
        self.length = len(self.dna)
        self.symbols = ['A','C','G','T']

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

    def minHammingDistance(self, kMer):
        minHammingDistance = len(kMer)
        for i in range(self.length - len(kMer) + 1):
            distance = self.hammingDistance(i, kMer)
            if distance < minHammingDistance:
                minHammingDistance = distance
        return minHammingDistance

    def minHammingDistancePositions(self, compareDNA, maxDistance):
        compateLength = len(compareDNA)
        indices = []
        for i in range(self.length - compateLength + 1):
            distance = self.hammingDistance(i, compareDNA)
            if distance <= maxDistance:
                indices.append(i)
        return indices
    
    def kMerExistsWithMaxHammingDistance(self, kMer, D):
        indices = self.minHammingDistancePositions(kMer, D)
        if len(indices) > 0:
            return True
        return False

    def howOftenkMerAppearsWithMinHammingDistance(self, kMer, minHammingDistance):
        count = 0
        for i in range(self.length - len(kMer) + 1):
            hammingDistance = self.hammingDistance(i, kMer)
            if hammingDistance <= minHammingDistance:
                count = count + 1
        return count

    def getAllPossibleKmers(self, length):
        return [''.join(i) for i in product(self.symbols, repeat = length)]

    def getAllKmersOfLength(self, length):
        kMers = []
        for i in range(self.length - length + 1):
            kMers.append(self.dna[i:i+length])
        return kMers

    def profielMostProbableKmer(self, k, profile):
        kMers = self.getAllKmersOfLength(k)
        mostProbable = 0
        mostProbablekMer = kMers[0]
        for kMer in kMers:
            probability = self.calculateProbabilityOfKmer(kMer, profile)
            if probability > mostProbable:
                mostProbable = probability
                mostProbablekMer = kMer
        return mostProbablekMer 

    def getSelfMostProbableKmer(self, profile, k):
        kMers = self.getAllKmersOfLength(k)
        mostProp = 0
        result = kMers[0]
        for kMer in kMers:
            prop = self.calculateProbabilityOfKmer(kMer, profile)
            if prop > mostProp:
                result = kMer
                mostProp = prop

        return result

    def calculateProbabilityOfKmer(self, kMer, profile):
        probability = 1
        for index, symbol in enumerate(kMer):
            if symbol == 'A':
                probability = probability * profile[0][index]
            elif symbol == 'C':
                probability = probability * profile[1][index]
            elif symbol == 'G':
                probability = probability * profile[2][index]
            elif symbol == 'T':
                probability = probability * profile[3][index]
        return probability

    def getProfileFromDNAs(self, dnas, t):
        dnaLength = len(dnas[0].getString())
        profile = np.zeros((4, dnaLength))
        for index in range(dnaLength):
            for myDna in dnas:
                dna = myDna.getString()
                symbol = dna[index]
                if symbol == 'A':
                    profile[0][index] = profile[0][index] + 1/t
                elif symbol == 'C':
                    profile[1][index] = profile[1][index] + 1/t
                elif symbol == 'G':
                    profile[2][index] = profile[2][index] + 1/t
                elif symbol == 'T':
                    profile[3][index] = profile[3][index] + 1/t
        return profile
