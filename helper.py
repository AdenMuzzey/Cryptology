
#list of all letters, then numbers
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
frequency = [ 8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074  ]
#https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
# E 	21912 	  	E 	12.02
# T 	16587 	  	T 	9.10
# A 	14810 	  	A 	8.12
# O 	14003 	  	O 	7.68
# I 	13318 	  	I 	7.31
# N 	12666 	  	N 	6.95
# S 	11450 	  	S 	6.28
# R 	10977 	  	R 	6.02
# H 	10795 	  	H 	5.92
# D 	7874 	  	D 	4.32
# L 	7253 	  	L 	3.98
# U 	5246 	  	U 	2.88
# C 	4943 	  	C 	2.71
# M 	4761 	  	M 	2.61
# F 	4200 	  	F 	2.30
# Y 	3853 	  	Y 	2.11
# W 	3819 	  	W 	2.09
# G 	3693 	  	G 	2.03
# P 	3316 	  	P 	1.82
# B 	2715 	  	B 	1.49
# V 	2019 	  	V 	1.11
# K 	1257 	  	K 	0.69
# X 	315 	  	X 	0.17
# Q 	205 	  	Q 	0.11
# J 	188 	  	J 	0.10
# Z 	128 	  	Z 	0.07


#converts a string of any characters to a string of only uppercase letters and numbers
def stripperWithNumbers(word):
    result = ""
    for c in word:
        if c.isdigit() or c.isalpha():
            result += c.upper()
    return result

def stripper(word):
    result = ""
    for c in word:
        if c.isalpha():
            result += c.upper()
    return result

def modInverse(a, m):
    for i in range(m):
        if (a % m) * (i % m) % m == 1:
            return i
    return -1

def myGCD(a, b):
    if a == 0:
        return b
    return myGCD(b % a, a)

def myExtendedGCD(a, b):
    if a == 0:
        return b, 0, 0, 1
    m, n, x1, y1 = myExtendedGCD(b%a, a)
    x = y1 - n/m * x1
    y = x1
    return m, n, x, y

# def chinese(x, y, result):
