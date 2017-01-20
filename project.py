UsedLetters = []
WordLength = 0
BadGuesses = 5
PlayerDisplay = []

def HideWord():
    count = 0
    while count != 50:
        print ('###')
        count += 1

def moveup():
    count = 0
    while count != 20:
        print ('')
        count += 1

def worddisplay(GuessL):
    count = 0
    goodguess = 0
    while count <= WordLength:
        if word[count] == (GuessL)[0]:
            PlayerDisplay[count] = (GuessL)[0]
            goodguess = 1
        count += 1

    if goodguess == 0:
        global BadGuesses
        BadGuesses = BadGuesses -1

def GameBody():
    Guess1 = input()
    Guess1L = list(Guess1)
    worddisplay(Guess1L)
    UsedLetters.append(Guess1)
    print ("Used Letters")
    print (UsedLetters)
    print ("Correct Letters")
    print (PlayerDisplay)
    print ('You have ' + str(BadGuesses) + ' guesses remaining')

print ('Welcome to Hangman')
print ('Please enter a word for your opponent to guess')
print ('This program is caps sensitive')


def GameStart():
    global WordLength
    global word
    WordToGuess = input("> ")
    HideWord()
    print ('Pass the program to your opponent, and press enter')
    moveup()
    input("Press Enter to continue")
    word = list(WordToGuess)
    for letters in WordToGuess:
        PlayerDisplay.append('_')
    print ("Start guessing!")
    print (PlayerDisplay)

    for letters in WordToGuess:
        WordLength += 1


    WordLength -= 1

    while BadGuesses != 0 and PlayerDisplay != word:
        GameBody()

    if PlayerDisplay == word:
        print ("Congratulations!")


    print ("The word was " + WordToGuess)
    print ("Try again?")
    input()


GameStart()
