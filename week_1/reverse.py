def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern


def Reverse(Pattern):
	string = ''
	for char in Pattern:
		string = char + string
	return string


def Complement(Pattern):
    dict = {'A':'T','G':'C','T':'A','C':'G'}
    return "".join(dict[i] for i in Pattern)

Pattern = 'GATTACA'
Reverse(Pattern)
Complement(Pattern)
print(ReverseComplement(Pattern))
