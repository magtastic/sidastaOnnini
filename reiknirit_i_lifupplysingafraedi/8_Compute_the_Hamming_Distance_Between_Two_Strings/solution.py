# coding=utf-8
import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path[:dir_path.rfind('/')] + '/0_Helper_Modules'
sys.path.insert(0, dir_path)
from DNAPatterns import DNA

DNA_STRING_1 = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
DNA_STRING_2 = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

myDNA = DNA(DNA_STRING_1)
print myDNA.hammingDistance(0, DNA_STRING_2)