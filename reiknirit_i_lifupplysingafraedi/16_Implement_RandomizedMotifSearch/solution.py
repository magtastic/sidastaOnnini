import numpy as np
import os, sys, random
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path[:dir_path.rfind('/')] + '/0_Helper_Modules'
sys.path.insert(0, dir_path)
from DNAPatterns import DNA

def generateProfileFromDNA(dna):
    baseMatrix = np.zeros((4, len(dna[0])))

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

def findAllProbMostKmersFromProfile(dnas, k, profile):
  motifs = []
  for dna in dnas:
    motifs.append(findProbMostKmersFromProfile(dna, k, profile))
  return motifs

def findProbMostKmersFromProfile(dna, k, profile):
  bestScore = 0
  bestPattern = dna[0:k]
  for i in range(len(dna) - k + 1):
      score = 1
      pattern = dna[i: i + k]
      for j in range(len(profile[0])):
          if pattern[j] == 'A':
              score = score * profile[0][j]
          if pattern[j] == 'C':
              score = score * profile[1][j]
          if pattern[j] == 'G':
              score = score * profile[2][j]
          if pattern[j] == 'T':
              score = score * profile[3][j]
      if score > bestScore:
          bestScore = score
          bestPattern = pattern
  return bestPattern


def randomlySelectKmers(dnas, k):
  result = []
  for dna in dnas:
    index = random.randrange(0,len(dna) - k + 1)
    result.append(dna[index:index+k])

  return result

def score(motifs):
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

def randomizedMotifSearch(dnas, k, t):
  motifs = randomlySelectKmers(dnas, k)
  bestMotifs = motifs
  bestScore = score(bestMotifs)

  i = 0
  while True:
    profile = generateProfileFromDNA(motifs)
    motifs = findAllProbMostKmersFromProfile(dnas, k, profile)
    motifScore = score(motifs)
    if motifScore < bestScore:
      bestMotifs = motifs
      bestScore = motifScore
      i = 0
    else:
      i += 1
    if i > 100:
      break

  print bestScore
  print bestMotifs



#==================================#
def readInfo():
  k, t = sys.stdin.readline().split(" ")
  k = int(k)
  t = int(t)
  dnas = []
  check = True
  while check:
      a = sys.stdin.readline().strip()
      if a != '':
          dnas.append(a)
      else:
          check = False
  return dnas, k, t

if __name__ == '__main__':
  dnas, k, t = readInfo()
  randomizedMotifSearch(dnas, k, t)
