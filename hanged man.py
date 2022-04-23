from ast import Break


good_drawing = [("----------"), ("|         "), ("|        "),("|        "),("|        "),("|        "),("|        "),("|        "),("|       "),("|_________")]
bad_drawing = [("----------"), ("|      |  "), ("|      |  "),("|      O  "),("|      |  "),("|  /  |  \ "),("|     | |  "),("|     | |  "),("|     - -  "),("|_________")]




def draw(guess_count, guessed_wrong):

    guess_count_local = guess_count
    guessed_wrong_local = guessed_wrong
    for i in range(guess_count_local):
        for i in range(guessed_wrong_local):
            print(bad_drawing[i])
            guess_count_local -= 1
            i += i
        i += i

def is_in_list(char, list):
    while(1):
        for i in range(len(list)):
            if(char == list[i]):
                break
            

    return 0

def run(secret_w):

    secret_word = secret_w
    guess_count = 10
    guessed_wrong = 0
    guessed_char = ''
    guessed_list = []
    guessed_secret = ""

    print("\n\n\n\n\n\n\n***Welcome to Hang-Man!***\nIt's time for you to guess our secret word of the Day!\n\n\n\n")
    
    

    while 1:
        guessed_char = str(input("Please make a guess!\n"))
        while(is_in_list(guessed_char)):
            guessed_char = str(input("Letter was already guessed.\nPlease make a new guess!\n"))


        if (is_in_list(guessed_char, secret_word)):
            print("Yes! " + guessed_char + " is part of the secret word!\n")
            
        draw(10, guessed_wrong)


run("Hallo")


print("***OMG YOU DID IT YOU MADLAD!!!***")


































































###THIS IS THE SHIT VERSION

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
