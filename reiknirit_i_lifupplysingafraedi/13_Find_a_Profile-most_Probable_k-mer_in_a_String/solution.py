import os, sys, numpy
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path[:dir_path.rfind('/')] + '/0_Helper_Modules'
sys.path.insert(0, dir_path)
from DNAPatterns import DNA

DNA_STRING = sys.stdin.readline().strip()
K = sys.stdin.readline().strip()
K = int(K)
PROFILE_LINE_1 = sys.stdin.readline().strip()
PROFILE_LINE_2 = sys.stdin.readline().strip()
PROFILE_LINE_3 = sys.stdin.readline().strip()
PROFILE_LINE_4 = sys.stdin.readline().strip()
EXPECTED = sys.stdin.readline().strip()



profile = numpy.zeros([4,K])
profile[0] = PROFILE_LINE_1.split(' ')
profile[1] = PROFILE_LINE_2.split(' ')
profile[2] = PROFILE_LINE_3.split(' ')
profile[3] = PROFILE_LINE_4.split(' ')

myDNA = DNA(DNA_STRING)
kMer = myDNA.profielMostProbableKmer(K, profile)


print 'EXPECTED: ', EXPECTED
print 'GOT: ', kMer
