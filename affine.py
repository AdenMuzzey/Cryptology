import helper

A = 5
B = 3

def affine(word):
    encrypt = ''
    word = helper.stripperWithNumbers(word)
    for c in word:
        temp = helper.characters.index(c)
        encrypt += helper.characters[(temp * A + B) % 36 ]
    print(encrypt)
    return encrypt

if __name__ == "__main__":
    affine("test.1234")
