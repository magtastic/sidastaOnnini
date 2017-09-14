import sys,collections

def HammingDistance(dna1, dna2):
	mCount = 0

	for i in range(len(dna1)):
		if dna1[i] != dna2[i]:
			mCount = mCount + 1

	return mCount

pattern = sys.stdin.readline().strip()
dna = sys.stdin.readline().strip()
d = int(sys.stdin.readline().strip())

r  = collections.defaultdict(int)

indexes = []

for i in range(len(dna) - len(pattern) + 1):
	if HammingDistance(dna[i: i + len(pattern)], pattern) <= d:
		indexes.append(i)

for i in indexes:
	print(i, end=' ')

