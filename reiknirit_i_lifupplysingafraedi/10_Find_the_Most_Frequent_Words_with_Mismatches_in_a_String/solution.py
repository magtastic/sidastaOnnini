# coding=utf-8
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path[:dir_path.rfind('/')] + '/0_Helper_Modules'
sys.path.insert(0, dir_path)
from DNAPatterns import DNA

DNA_STRING = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
K_AND_D = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
EXPECT = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

K = int(K_AND_D.split()[0])
D = int(K_AND_D.split()[1])
myDNA = DNA(DNA_STRING)
print myDNA.getString()
print K
print D
print EXPECT
print myDNA.kMersWithMinHammingDistance(K,D)
