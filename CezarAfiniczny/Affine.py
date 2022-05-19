def encrypt():

    f = open("plain.txt", "r")
    text = f.read()
    f.close()
    f = open("key.txt", "r")
    keys = f.read().split(" ")
    for i in range(0, len(keys)):
        keys[i] = int(keys[i])
    f.close()
    inverse = modularInverse(keys[0], 26)

    if gcd(keys[0], keys[1]) != 1:
        raise Exception("Zły klucz")
    if (keys[0] * inverse) % 26 != 1:
        raise Exception("Zły klucz")

    result = ""

    for i in range(len(text)):
        ch = text[i]
        if ch.isupper():
            result += chr((((ord(ch) - ord('A')) * keys[0] + keys[1]) % 26) + ord('A'))
        elif ch == ' ':
            result += ' '
        elif not ord('A') <= ord(ch) <= ord('Z') and not ord('a') <= ord(ch) <= ord('z'):
            result += ch
        else:
            result += chr((((ord(ch) - ord('a')) * keys[0] + keys[1]) % 26) + ord('a'))

    f = open("crypto.txt", "w+")
    f.write(result)
    f.close()


def decrypt():

    f = open("crypto.txt", "r")
    cipher = f.read()
    f.close()
    f = open("key.txt", "r")
    keys = f.read().split(" ")
    for i in range(0, len(keys)):
        keys[i] = int(keys[i])
    f.close()
    inverse = modularInverse(keys[0], 26)

    if not inverse:
        raise Exception("Zły klucz")
    if (keys[0] * inverse) % 26 != 1:
        raise Exception("Zły klucz")

    result = ""

    for i in range(len(cipher)):
        ch = cipher[i]
        if ch.isupper():
            result += chr(((inverse*(ord(ch) - ord('A') - keys[1])) % 26) + ord('A'))
        elif ch == ' ':
            result += ' '
        elif not ord('A') <= ord(ch) <= ord('Z') and not ord('a') <= ord(ch) <= ord('z'):
            result += ch
        else:
            result += chr(((inverse*(ord(ch) - ord('a') - keys[1])) % 26) + ord('a'))

    f = open("plain.txt", "w+")
    f.write(result)
    f.close()


def analiseWithText():
    return


def analizeWithCryptogram():
    f = open("crypto.txt", "r")
    cipher = f.read()
    f.close()

    result = ""

    for i in range(1, 26):
        for j in range(0, 26):
            inverse = modularInverse(i, 26)
            if not inverse:
                continue
            if (i * inverse) % 26 != 1:
                continue
            for k in range(len(cipher)):
                ch = cipher[k]
                if ch.isupper():
                    result += chr(((inverse*(ord(ch) - ord('A') - j)) % 26) + ord('A'))
                elif ch == ' ':
                    result += ' '
                elif not ord('A') <= ord(ch) <= ord('Z') and not ord('a') <= ord(ch) <= ord('z'):
                    result += ch
                else:
                    result += chr(((inverse*(ord(ch) - ord('a') - j)) % 26) + ord('a'))

            result += "\n"

    f = open("plain.txt", "w+")
    f.write(result)
    f.close()


def modularInverse(a, m):
    for i in range(1, m):
        if (m * i + 1) % a == 0:
            return (m * i + 1) // a
    return None


def gcd(a, b):
    while b:
        c = a % b
        a = b
        b = c
    return a