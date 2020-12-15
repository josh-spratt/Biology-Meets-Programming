import matplotlib.pyplot as plt


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

    
with open('e_coli.txt') as file:
    genome = file.read()
    skew = SkewArray(genome)
    plt.plot(skew)
    plt.xlabel('genome position')
    plt.ylabel('skew')
    plt.show()
