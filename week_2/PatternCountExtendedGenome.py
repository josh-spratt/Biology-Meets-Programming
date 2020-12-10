#import sys
#input = sys.stdin.read().splitlines()
#e_coli = input[1]


def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array


def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]
        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array


def PatternCount(symbol, ExtendedGenome):
   count = 0
   for i in range(len(ExtendedGenome)-len(symbol)+1):
       if ExtendedGenome[i:i+len(symbol)] == symbol:
           count = count+1
   return count


def SkewArray(Genome):
    Skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            Skew.append(Skew[i] - 1)
        elif Genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        else:
            Skew.append(Skew[i])
    return Skew


def MinimumSkew(Genome):
    array = SkewArray(Genome)
    positions = []
    count = 0
    min_array = min(array)
    for i in array:
        if i == min_array:
            positions.append(count)
        count += 1
    return positions

Genome = 'CATGGGCATCGGCCATACGCC'
print(SkewArray(Genome))
print(MinimumSkew(Genome))
