from ast import Break
from random import randint
import os
clear = lambda: os.system('cls')
import time

good_drawing = [("----------"), ("|         "), ("|        "),("|        "),("|        "),("|        "),("|        "),("|        "),("|       "),("|_________")]
bad_drawing = [("----------"), ("|      |  "), ("|      |  "),("|      O  "),("|     /|\ "),("|    / | \ "),("|     | |  "),("|     | |  "),("|     - -  "),("|_________")]

dictionary = [("time" ),("person" ),("year" ),("way" ),("day" ),("thing" ),("man" ),("world" ),("life" ),("hand" ),("part" ),("child" ),("eye" ),("woman" ),("place" ),("work" ),("week" ),("case" ),("point" ),("government" ),("company" ),("number" ),("group" ),("problem" ),("fact" )]


def draw(guess_count, guessed_wrong):

    guess_count_local = guess_count
    guessed_wrong_local = guessed_wrong+1
    for i in range(guessed_wrong_local):
        print(bad_drawing[i])
        i += 1
    j=0
    j+=guessed_wrong_local
    while(j < guess_count_local):
        print(good_drawing[j])
        j += 1

def is_in_list(char, list, list_to_be_altered=[]):
    amount = 0
    for i in range(len(list)):
        if(char == list[i]):
            if(list_to_be_altered!=[]):
                list_to_be_altered[i]=char
            amount+=1
    return amount

def run(secret_w):

    secret_word = list(secret_w)
    #guess_count = 10
    guessed_wrong = 0
    guessed_char = ""
    guessed_list = []
    guessed_secret = [] 
    for i in secret_word:
        guessed_secret.append('*')

    print("\n***Welcome to Hang-Man!***\nIt's time for you to guess our secret word of the Day!\n\n")
    
    

    while guessed_list != secret_word:
        print(guessed_secret)
        guessed_char = str(input("\nPlease make a guess!\n"))[0].lower()
        while(is_in_list(guessed_char, guessed_list)>0):
            clear()
            print(guessed_secret)
            guessed_char = str(input("Letter was already guessed.\nPlease make a new guess!\n"))[0].lower()
        guessed_list.append(guessed_char)


        if (is_in_list(guessed_char, secret_word, guessed_secret)>0):
            clear()
            print("Yes! " + guessed_char + " is part of the secret word!\n")
            print(guessed_secret)


        else: 
            guessed_wrong+=1
            clear()
            draw(10, guessed_wrong)
            
        
        if(guessed_wrong>=8):
            print("Exceeded 10 guesses :( guess you suck..\n")
            return
        elif(guessed_secret == secret_word):
            break
    clear()
    print("\n\n\n\n-----------------------------------------------\n|\t\t\t\t\t\t|\n|\t\t\t\t\t\t|")
    print("|\t***OMG YOU DID IT YOU MADLAD!!!***\t|")
    print("|\t\t\t\t\t\t|\n|\t\t\t\t\t\t|\n----------------------------------------------\n\n")
    for i in (1,2,3,4,5):
        print('.', end='', flush=True)
        time.sleep(1)

while(1):
    clear()
    x = 0
    x = int(input("Please choose a gamemode!\n1)\tRandom Word\n2)\t2 Players - 1 chooses, 1 guessed\nEnter x to exit.\n"))
    if(x == 1):
        clear()
        print("\nGeneration Random Word...")
        run(dictionary[randint(0,len(dictionary)-1)].lower())
        for i in (1,2,3,4,5):
            print('.', end='', flush=True)
            time.sleep(1)
    elif(x == 2):
        while(1):
            user_word = str(input("\nPlease provide a word to be guesses!\n")).lower()
            if(user_word.isalpha()):
                clear()
                run(user_word)
                break
            else:
                print("Invalid Input, nice try though.\n")
                continue

    elif(x == "x"):
        print("\nThx for playing!\n")
        break
    else:
        print("Not a valid input.")
        continue