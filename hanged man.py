from ast import Break
from random import randint



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

    print("\n\n\n\n\n\n\n***Welcome to Hang-Man!***\nIt's time for you to guess our secret word of the Day!\n\n\n\n")
    
    

    while guessed_list != secret_word:
        guessed_char = str(input("\nPlease make a guess!\n"))[0].lower()
        while(is_in_list(guessed_char, guessed_list)>0):
            guessed_char = str(input("Letter was already guessed.\nPlease make a new guess!\n"))[0].lower()
        guessed_list.append(guessed_char)


        if (is_in_list(guessed_char, secret_word, guessed_secret)>0):
            print("Yes! " + guessed_char + " is part of the secret word!\n")
            print(guessed_secret)


        else: 
            guessed_wrong+=1
            draw(10, guessed_wrong)
        
        if(guessed_wrong>=8):
            print("Exceeded 10 guesses :( guess you suck..\n")
            return
        elif(guessed_secret == secret_word):
            break
    print("\n\n-----------------------------------------------\n|\t\t\t\t\t\t|\n|\t\t\t\t\t\t|")
    print("|\t***OMG YOU DID IT YOU MADLAD!!!***\t|")
    print("|\t\t\t\t\t\t|\n|\t\t\t\t\t\t|\n----------------------------------------------\n\n")

while(1):
    x = 0
    x = int(input("Please choose a gamemode!\n0)\tRandom Word\n1)\t2 Players - 1 chooses, 1 guesses\nEnter 3 to exit.\n"))
    if(x == 0):
        print("\nGeneration Random Word...")
        run(dictionary[randint(0,len(dictionary)-1)].lower())
    elif(x == 1):
        while(1):
            user_word = str(input("\nPlease provide a word to be guesses!\n")).lower()
            if(user_word.isalpha):
                run(user_word)
                break
            else:
                print("Invalid Input, nice try though.\n")
                continue

    elif(x == 3):
        print("\nThx for playing!\n")
        break
    else:
        print("Not a valid input.")
        continue