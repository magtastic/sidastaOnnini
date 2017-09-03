# coding=utf-8
import sys

DNA = sys.stdin.readline().strip() #sys.readline() les linu, strip() fjarlægir enter merki

def countACGT(text):
    A = 0
    C = 0
    G = 0
    T = 0
    for symbol in text:
        if symbol == 'A':
            A = A + 1
        elif symbol == 'C':
            C = C + 1
        elif symbol == 'G':
            G = G + 1
        elif symbol == 'T':
            T = T + 1
    return A, C, G, T


print countACGT(DNA)
