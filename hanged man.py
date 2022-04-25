from ast import Break



good_drawing = [("----------"), ("|         "), ("|        "),("|        "),("|        "),("|        "),("|        "),("|        "),("|       "),("|_________")]
bad_drawing = [("----------"), ("|      |  "), ("|      |  "),("|      O  "),("|      |  "),("|   /  |  \ "),("|     | |  "),("|     | |  "),("|     - -  "),("|_________")]




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
        guessed_char = str(input("\nPlease make a guess!\n"))[0]
        while(is_in_list(guessed_char, guessed_list)>0):
            guessed_char = str(input("Letter was already guessed.\nPlease make a new guess!\n"))[0]
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



run("mama")