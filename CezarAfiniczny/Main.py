# Autor: Przemysław Sankowski
#
# Polskie znaki nie są obsługiwane w ogóle - jeśli znajdą się w plain.txt po prostu nie zostaną zaszyfrowane.
# Funkcja -j (kryptoanaliza z tekstem jawnym) dla szyfru afinicznego nie jest zaimplementowana.
# Wykonanie powyższej funkcji dla szyfru cezara nadpisze plik key.txt pojedynczą cyfrą, a więc, żeby program działał dla szyfru
# afinicznego po wykonaniu kryptoanalizy z tekstem jawnym dla cezara, trzeba wprowadzić drugą cyfrę klucza ręcznie.

import Cesar as c
import Affine as a
import sys

print(sys.argv[0], sys.argv[1])

if sys.argv[0] == '-c':
    if sys.argv[1] == '-e':
        c.encrypt()
    elif sys.argv[1] == '-d':
        c.encrypt()
    elif sys.argv[1] == '-j':
        c.encrypt()
    elif sys.argv[1] == '-k':
        c.encrypt()

if sys.argv[0] == '-a':
    if sys.argv[1] == '-e':
        a.encrypt()
    elif sys.argv[1] == '-d':
        a.encrypt()
    elif sys.argv[1] == '-j':
        a.encrypt()
    elif sys.argv[1] == '-k':
        a.encrypt()


# def menu():
#     x = input("Wybierz szyfr: \nc - Cezara, \na - Afiniczny\nLub:\nx - wyjdz z programu\n")
#     if x == 'c':
#         secondMenu(x)
#     elif x == 'a':
#         secondMenu(x)
#     elif x == 'x':
#         return
#     else:
#         print("\nNiepoprawna opcja\n")
#         menu()
#
#
# def secondMenu(arg):
#     x = input("Wybierz opcje: \ne - szyfrowanie, \nd - odszyfrowywanie,"
#               "\nj - kryptoanaliza z tekstem jawnym, "
#               "\nk - kryptoanaliza wyłącznie w oparciu o kryptogram, "
#               "\nz - wróć do wyboru szyfru\n")
#     if x == 'e' and arg == 'c':
#         c.encrypt()
#         menu()
#     elif x == 'd' and arg == 'c':
#         c.decrypt()
#         menu()
#     elif x == 'j' and arg == 'c':
#         c.analiseWithText()
#         menu()
#     elif x == 'k' and arg == 'c':
#         c.analizeWithCryptogram()
#         menu()
#     elif x == 'e' and arg == 'a':
#         a.encrypt()
#         menu()
#     elif x == 'd' and arg == 'a':
#         a.decrypt()
#         menu()
#     elif x == 'j' and arg == 'a':
#         a.analiseWithText()
#         menu()
#     elif x == 'k' and arg == 'a':
#         a.analizeWithCryptogram()
#         menu()
#     elif x == 'z':
#         menu()
#     else:
#         print("\nNiepoprawna opcja\n")
#         secondMenu(arg)
#
# menu()