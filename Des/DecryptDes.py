import EncryptDes

def decryptDes(message, key):
    r, l = message // 64, message % 64
    k = key + (key * 512)
    for x in range(4):
        bit = k // (2 ** (7 + x)) % 256
        l, r = r, EncryptDes.f(r, bit) ^ l
    return r * 64 + l

if __name__ == "__main__":
    # print (f(23, 164)) # should be 4
    test = EncryptDes.des(475, 77)
    print (decryptDes(test, 77))