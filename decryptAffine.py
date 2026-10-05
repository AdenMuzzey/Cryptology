import helper
import affine

def decryptAffine(word):
    dencrypt = ''
    # word = helper.stripper(word)
    for c in word:
        temp = helper.characters.index(c)
        dencrypt += helper.characters[((temp - affine.B) * helper.modInverse(affine.A, 36)) % 36]
    print(dencrypt)

if __name__ == "__main__":
    word = affine.affine("test.1234")
    decryptAffine(word)
