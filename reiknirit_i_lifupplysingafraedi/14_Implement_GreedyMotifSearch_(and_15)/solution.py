import sys, collections, math
import numpy as np


# Takes in an array of string, returns a matrix of probability
def GenerateProfMatrix(dna, L):
    # Create a matrix to count the number of bases at each position in the DNA strings
    if L:
        baseMatrix = np.ones((4, len(dna[0])))
    else:
        baseMatrix = np.zeros((4, len(dna[0])))

    # For each string in dna, mark what base is at what position and add it to the base matrix count
    for i in range(len(dna)):
        for j in range(len(dna[0])):
            if dna[i][j] == 'A':
                baseMatrix[0][j] = baseMatrix[0][j] + 1
            if dna[i][j] == 'C':
                baseMatrix[1][j] = baseMatrix[1][j] + 1
            if dna[i][j] == 'G':
                baseMatrix[2][j] = baseMatrix[2][j] + 1
            if dna[i][j] == 'T':
                baseMatrix[3][j] = baseMatrix[3][j] + 1

    profileMatrix = np.divide(baseMatrix, len(dna))

    return profileMatrix


# Takes in a dna string, integer k and a 4 x k matrix
def FindProbProfile(dna, k, prob):
    bestScore = 0
    bestPattern = dna[0:k]

    for i in range(len(dna) - k + 1):
        score = 1
        pattern = dna[i: i + k]
        for j in range(len(prob[0])):
            if pattern[j] == 'A':
                score = score * prob[0][j]
            if pattern[j] == 'C':
                score = score * prob[1][j]
            if pattern[j] == 'G':
                score = score * prob[2][j]
            if pattern[j] == 'T':
                score = score * prob[3][j]

        if score > bestScore:
            bestScore = score
            bestPattern = pattern

    return bestPattern

# Calculates the score for a set of motifs
def Score(motifs):
    score = 0
    for i in range(len(motifs[0])):
        baseCount = [0,0,0,0]
        for j in range(len(motifs)):
            if motifs[j][i] == 'A':
                baseCount[0] = baseCount[0] + 1
            if motifs[j][i] == 'C':
                baseCount[1] = baseCount[1] + 1
            if motifs[j][i] == 'G':
                baseCount[2] = baseCount[2] + 1
            if motifs[j][i] == 'T':
                baseCount[3] = baseCount[3] + 1
        score = score + (len(motifs) - max(baseCount))
    return score

k, t = sys.stdin.readline().split(" ")
k = int(k)
t = int(t)

dna = []
check = True

# Read in the lines of DNA
while check:
    a = sys.stdin.readline().strip()
    if a != '':
        dna.append(a)
    else:
        check = False

bestMotifScore = float('inf')
bestMotifs = []
# Iterate through each k-mer in dna[0] as the starting motif
for j in range(len(dna[0])-k+1):
    motifs = np.array([dna[0][j:j+k]])
    for i in range(1, len(dna)):
        profMatrix = GenerateProfMatrix(motifs, True)
        motifs = np.append(motifs, FindProbProfile(dna[i], k, profMatrix))

    score = Score(motifs)
    if score < bestMotifScore:
        bestMotifScore = score
        bestMotifs = motifs

for i in bestMotifs:
    print(i)
