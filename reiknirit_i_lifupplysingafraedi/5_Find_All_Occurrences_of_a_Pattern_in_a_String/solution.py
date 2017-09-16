# coding=utf-8
import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path[:dir_path.rfind('/')] + '/0_Helper_Modules'
sys.path.insert(0, dir_path)
from DNAPatterns import DNA

PATTERN = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki
DNA_STRING = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

myDNAString = DNA(DNA_STRING)
indexes = []
for i, c in enumerate(myDNAString.getString()):
    if myDNAString.text(i, len(PATTERN)) == PATTERN:
        indexes.append(i)

print indexes