from abc import ABC
from curses import ACS_BBSS


def word_combos(letters):
    letters_copy = letters.copy()
    for letter in letters_copy:
        for j in letters_copy:

            print(letter+j)
    return 

list_words = ["A", "B", "C"] = 12 
word_combos(list_words)
ABC
ACB
AB
AC
BCA
BAC
BA
BC
CAB
CBA
CA
CB

ABCD 