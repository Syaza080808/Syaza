#!/usr/bin/env python

import random

def main():
 """Start guessing the name of song (2023 era only)"""
 print("Guess the name of song, the singer  and genre(2023 era only gurlll)")

 x = str("In ha mood by ice spice pop genre")
 guess = None

 while x != guess:

    guess = str(input("guess a 2023 era song, singer and genre: "))

    if x == guess:
        print("You deserve to be a gen-z!")
    else :
        print("another hint for you, its a female rapper,only the starting letter is caps lock and the singers hair is orange")
exit
main()