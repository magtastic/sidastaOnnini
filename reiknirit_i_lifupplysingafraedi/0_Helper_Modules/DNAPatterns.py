# coding=utf-8
class DNA:
    def __init__(self, dnaString):
        self.dna = dnaString
    
    def getString(self):
        return self.dna

    def text(self, i, k):
        return self.dna[i:i+k]

    def count(self, pattern):
        pattLen = len(pattern)
        count = 0
        for i, _ in enumerate(self.dna[:len(self.dna)-pattLen]):
            if self.text(i,pattLen) == pattern:
                count = count + 1
        return count

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


    
