# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    profile = Count(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    for i in profile.keys():
        for j in range(k):
            profile[i][j] /= t
    return profile


# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    consensus = Consensus(Motifs)
    count = 0
    for motif in Motifs:
        for index in range(len(motif)):
            if motif[index] != consensus[index]:
                count += 1
    return count


# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p*Profile[Text[i]][i]
    return p


def ProfileMostProbableKmer(Text, k, Profile):
    max_prob = 0
    most_probable = Text[:k]
    n = len(Text)
    for i in range(n - k + 1):
        kmer = Text[i: i + k]
        probability = Pr(kmer, Profile)
        if probability > max_prob:
            max_prob = probability
            most_probable = kmer
    return most_probable


# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


profile = {'A': [0.4,  0.3,  0.0,  0.1,  0.0,  0.9], 'C': [0.2,  0.3,  0.0,  0.4,  0.0,  0.1], 'G': [
    0.1,  0.3,  1.0,  0.1,  0.5,  0.0], 'T': [0.3,  0.1,  0.0,  0.4,  0.5,  0.0]}
answer = Pr('AAGTTC', profile)
print(answer)
