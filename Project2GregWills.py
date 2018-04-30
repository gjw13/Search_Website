#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:57:34 2018

@author: gjwills
"""

import requests
import nltk

# ****** main function that handles most user input, calls helper functions ****
def main():
    searchedWords = []
    anotherWebsite = True; # boolean to determine if user wants to scrape
                           # another website
    while anotherWebsite == True:
        
        # Good front-end interface with user
        print("Please enter a URL for a website. Be sure to include the",end=" ")
        print("http://. For example, your URL may look like http://",end="")
        print("www.georgetown.edu.")
        
        # Function returns URL inputted by user
        URL = getURL()
        
    
        # turn words from page source into list, URL is entered correctly
        # wordList = scrapeWebsite(URL)
        
        # EXTRA CREDIT FUNCTION using NLTK
        wordList = useNLTK(URL)
    
        # Print first ten words by calling firstTenWords() function
        print("\nHere are the first ten words on the website: ", end="")
        print(firstTenWords(wordList))
    
        # Ask for keyword to count
        anotherWord = True # boolean to determine whether user wants to search for another word
        
        # while loop to search for word in URl previously entered
        while anotherWord == True:
            print("\nThanks! Next, enter a keyword you want to search for and ",end="")
            wordToFind = input("count for on your website: ")
            searchedWords.append(wordToFind);
            # print out the word, the site, and the count of word appearances
            print("Great, the word", wordToFind, "occurs on the site,", URL, end=", ")
            word_count = wordCount(wordList, wordToFind)
            print(word_count, end = " ")
            # handling if the word only appears once
            if word_count == 1:
                print("time\n")
            else:
                print("times\n")
            
            # Dealing with another word to search for
            print("Do you want to enter another word to search for on",end=" ")
            print("the site,", URL, end="?")
            validInput = True
            while validInput == True:
                cont = input("> ")
                if cont.lower() == "yes" or cont.lower() == "y":
                    # print("You did it...")
                    validInput = False # exits the loop then and returns to outer while loop
                elif cont.lower() == "no" or cont.lower() == "n":
                    summary(searchedWords)
                    del searchedWords[:]
                    c = input("Ok, do you want to enter a different URL to search? ")
                    anotherWord = False # will prompt user with website while loop, exits 2 loops
                    if c.lower() == "yes":
                        anotherWebsite = True
                        validInput = False
                    elif c.lower() == "no":
                        # this will exit the program by breaking out of all loops
                        anotherWebsite = False
                        print("Thanks for using my program! Goodbye!")
                        validInput = False
                    else:
                        print("Invalid input...Type yes or no")
                        validInput = True
                        
                else:
                    print("Invalid input...Type yes or no")
       
# ******* function returns URL inputted by the user             
def getURL():
    URL = input("URL: ") # take URL in for scraping
    
    # error checking in user URL
    while URL[0:7] != "http://":
        print("Uh-oh! Your URL was entered incorrectly. ")
        URL = input("Please try again: ")
    return URL
                
# ******* returns list of words delimited by space from website *****
def scrapeWebsite(site):
    response = requests.get(site)
    txt = response.text # txt is the string with html code
    Words = txt.split(" ") # split txt delimited with a space
            
    return Words
    
# ****** returns count of the words on the website given user entered word *****
def wordCount(Words, word):
    count = 0
    # length = len(word)
    for item in Words:
        # if you wanted to search for a substring, you can use 'in' function
        if word.lower() in item.lower():
            c = item.lower().count(word.lower()) # count number of substrings
            count = count + c # add subtring count to count
#        if word.lower() in item.lower():
#            count+=1
    
    return count
    
# ***** given list of strins, function will return first 10 strings ****** 
def firstTenWords(wordList):
    # return wordList[:10]
    print("\n")
    for item in range(0,10):
        print("[",item+1,"]: ",wordList[item])
# I couldn't figure out why None was printing after printing the first ten words

#    print(wordList[:10])

# ***** this function takes in a list of words that were searched for by the user ****
def summary(searchedWords):
    print("Here is the list of words you searched on this site.")
    print(searchedWords)
        
def useNLTK(site):
    # Extra credit function that uses NLTK package to tokenize words
    # It gets the same results as you would with the normal function.
    # There are a few lines below that make the words more elegant.
    # The function that counts the word on the site remains the same.
    response = requests.get(site)
    txt = response.text
    words = nltk.word_tokenize(txt)
    
    # code below was borrowed from https://www.strehle.de/tim/weblog/archives/2015/09/03/1569
    # remove one character words
    words = [word for word in words if len(word) > 1]
    
    # remove numeric characters
    words = [word for word in words if not word.isnumeric()]
    
    # make all words lowercase
    words = [word.lower() for word in words]
    
    return words
    
main()