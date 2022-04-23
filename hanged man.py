""""
character_name = "Peter"
character_age = "80"

print("His Name was " + character_name + ", he died at the age of " + character_age + ".\n")

repeat = input("Enter something to repeat please :)\n")
print("repeating..\n" + repeat + "\n\n")
"""
"""
character_list = []
character_list.append(input("Type the Name of your first Character.\n"))
character_list.append(input("Type the Name of your second Character.\n"))
character_list.append(input("Type the Name of your third Character.\n"))
print("Repeating the CharacterList in order now!\n")
print(character_list[0:])

"""
























"""

good_drawing = [("----------"), ("|      |  "), ("|      |  "),("|      O  "),("|      |  "),("|    /   \ "),("|      |  "),("|     | |  "),("|     - -  "),("|_________")]

def draw(x):
    for i in range(x):
        print(good_drawing[i])
        i += i



def run(secret_w):
    guess_count = 0
    guessed_word = "NONE"
    secret_word = secret_w
    print("\n\n\n\n\n\n\n***Welcome to Hang-Man!***\nIt's time for you to guess our secret word of the Day!\n\n\n\n")
    guessed_word = str(input("Please make a guess!\n"))
    while guessed_word != secret_word:
        guess_count += 1
        draw(guess_count)
        guessed_word = str(input("Please make a guess!\n"))


run("Hallo")
print("***OMG YOU DID IT YOU MADLAD!!!***")


"""
















good_drawing = [("----------"), ("|         "), ("|        "),("|        "),("|        "),("|        "),("|        "),("|        "),("|       "),("|_________")]
bad_drawing = [("----------"), ("|      |  "), ("|      |  "),("|      O  "),("|      |  "),("|  /  |  \ "),("|     | |  "),("|     | |  "),("|     - -  "),("|_________")]

def draw(guess_count, guessed_wrong):
    guess_count_local = guess_count
    guessed_wrong_local = guessed_wrong
    for i in range(guess_count_local):
        for i in range(guessed_wrong_local):
            print(bad_drawing[i])
            guess_count_local -= guess_count_local
            i += i
        i += i



def is_in_list(char, list):
    for i in range(len(list)):
        if(char == list[i]):
            return 1
    return 0




def run(secret_w):

    secret_word = secret_w
    guess_count = 0
    guessed_wrong = 0
    guessed_char = ''
    guessed_list = []
    guessed_secret = ""

    print("\n\n\n\n\n\n\n***Welcome to Hang-Man!***\nIt's time for you to guess our secret word of the Day!\n\n\n\n")
    
    while 1:
        guessed_char = str(input("Please make a guess!\n"))
        while(is_in_list(guessed_char)):
            guessed_char = str(input("Letter was already guessed.\nPlease make a new guess!\n"))
        guess_count += 1
        if (is_in_list(guessed_char, secret_word)):
            return
        draw(guess_count)


run("Hallo")


print("***OMG YOU DID IT YOU MADLAD!!!***")
