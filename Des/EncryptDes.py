
S1 = [0b101, 0b010, 0b001, 0b110, 0b011, 0b100, 0b111, 0b000, 0b001, 0b100, 0b110, 0b010, 0b000, 0b111, 0b101, 0b011]
S2 = [0b100, 0b000, 0b110, 0b101, 0b111, 0b001, 0b011, 0b010, 0b101, 0b011, 0b000, 0b111, 0b110, 0b010, 0b001, 0b100]

def f(r, k):
    b = format(r, '06b')
    expanded = int(b[0])*128 + int(b[1])*64 + int(b[3])*32 + int(b[2])*16 + int(b[3])*8 + int(b[2])*4 + int(b[4])*2 + int(b[5])
    result = expanded ^ k
    return S1[result // 16] * 8 + S2[result % 16]

def des(message, key):
    l, r = message // 64, message % 64
    k = key + (key * 512)
    for x in range(4):
        bit = k // (2 ** (10 - x)) % 256
        l, r = r, f(r, bit) ^ l
    return l * 64 + r

if __name__ == "__main__":
    # print (f(23, 164)) # should be 4
    print (des(475, 77))