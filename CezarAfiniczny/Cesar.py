def encrypt():

    f = open("plain.txt", "r")
    text = f.read()
    f.close()
    f = open("key.txt", "r")
    key = int(f.read().split()[0])
    f.close()

    if key < 0 or key > 25:
        raise Exception("Zły klucz")

    result = ""

    for i in range(len(text)):
        ch = text[i]
        if ch.isupper():
            result += chr((ord(ch) + key - ord('A')) % 26 + ord('A'))
        elif ch == ' ':
            result += ' '
        elif not ord('A') <= ord(ch) <= ord('Z') and not ord('a') <= ord(ch) <= ord('z'):
            result += ch
        else:
            result += chr((ord(ch) + key - ord('a')) % 26 + ord('a'))

    f = open("crypto.txt", "w+")
    f.write(result)
    f.close()


def decrypt():

    f = open("crypto.txt", "r")
    cipher = f.read()
    f.close()
    f = open("key.txt", "r")
    key = int(f.read().split()[0])
    f.close()

    if key < 0 or key > 26:
        raise Exception("Zły klucz")

    result = ""

    for i in range(len(cipher)):
        ch = cipher[i]
        if ch.isupper():
            result += chr((ord(ch) - key - ord('A')) % 26 + ord('A'))
        elif ch == ' ':
            result += ' '
        elif not ord('A') <= ord(ch) <= ord('Z') and not ord('a') <= ord(ch) <= ord('z'):
            result += ch
        else:
            result += chr((ord(ch) - key - ord('a')) % 26 + ord('a'))

    f = open("plain.txt", "w+")
    f.write(result)
    f.close()


def analiseWithText():
    f = open("extra.txt", "r")
    text = f.read()
    f.close()
    f = open("crypto.txt", "r")
    cipher = f.read()
    f.close()

    ch1 = text[0]
    ch2 = cipher[0]
    key = (ord(ch2) - ord(ch1)) % 26
    ch1 = text[1]
    ch2 = cipher[1]

    if (ord(ch2) - ord(ch1)) % 26 != key:
        raise Exception("Nie da się znaleźć klucza")

    f = open("key.txt", "w+")
    f.write(str(key))
    f.close()

    result = ""

    for i in range(len(cipher)):
        ch = cipher[i]
        if ch.isupper():
            result += chr((ord(ch) - key - ord('A')) % 26 + ord('A'))
        elif ch == ' ':
            result += ' '
        elif not ord('A') <= ord(ch) <= ord('Z') and not ord('a') <= ord(ch) <= ord('z'):
            result += ch
        else:
            result += chr((ord(ch) - key - ord('a')) % 26 + ord('a'))

    f = open("plain.txt", "w+")
    f.write(result)
    f.close()



def analizeWithCryptogram():
    f = open("crypto.txt", "r")
    cipher = f.read()
    f.close()

    result = ""

    for i in range(1, 26):
        for j in range(len(cipher)):
            ch = cipher[j]
            if ch.isupper():
                result += chr((ord(ch) - i - ord('A')) % 26 + ord('A'))
            elif ch == ' ':
                result += ' '
            elif not ord('A') <= ord(ch) <= ord('Z') and not ord('a') <= ord(ch) <= ord('z'):
                result += ch
            else:
                result += chr((ord(ch) - i - ord('a')) % 26 + ord('a'))

        result += "\n"

    f = open("plain.txt", "w+")
    f.write(result)
    f.close()