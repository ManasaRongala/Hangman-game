# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:17:13 2017

@author: satyam
"""
# Hangman game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    handle = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = handle.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    
    
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far.....
    returns: boolean, return True if all the letters of secretWord are in lettersGuessed;
      otherwise False
    '''
    b=[]
    for i in lettersGuessed:
             if i in secretWord:
                    b = b+[i,]
    sortedlettersGuessed = sorted(b)

    sortedSecretWord = sorted(secretWord)

    if sortedSecretWord == sortedlettersGuessed:
       a=True
    else:
       a=False
    return a
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word that user is guessing
    lettersGuessed: list, what letters have been guessed so far.....
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    a=""
    for i in secretWord:
       if i in lettersGuessed:
                a=a+i
       else:
                a=a+" _"
    return a


alphabet=string.ascii_lowercase
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far.....
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    newAlphabet = ""
    for i in alphabet:
        if i not in lettersGuessed:
            newAlphabet = newAlphabet+i
    return newAlphabet


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    p = " _"
    numGuesses=8
    lettersGuessed=[]
    lengthSecretWord=len(secretWord)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(lengthSecretWord)+" letters long.")
    print(p*lengthSecretWord)
    
    guessing=True
    while guessing:
    
       print("You have "+str(numGuesses)+" guesses left.")
       print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
       letterGuessed = input("Guess a letter: ")
       lowerletterGuessed = letterGuessed.lower()
       lettersGuessed = lettersGuessed+[lowerletterGuessed,]
       

       if letterGuessed in secretWord:
           print("Good guess: "+str(getGuessedWord(secretWord, lettersGuessed)))
           if isWordGuessed(secretWord,lettersGuessed):
               print("Congratulations, you won! the Game, Well played....")
               break
          
           
       else:
          numGuesses=numGuesses-1
          print("Oops! That letter is not in word: "+str(getGuessedWord(secretWord, lettersGuessed)))
          if numGuesses==0:
                  print("Sorry, you ran out of number of guesses. The word was "+str(secretWord))
                  break
       

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

