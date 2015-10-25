nice = 0
mean = 0

def main():
    start()

def bad_lang():
    print "You aren't speaking my language. Automatic ejection from the game!"
    exit()

def start():
    print "Hello! Welcome to Nice or Mean..."
    name = raw_input("What is your name? : ")
    print "Hi, "+name+"! So nice to meet you... well maybe. We will find out, won't we?"
    print "In this game, you will be greeted by several different people..."
    print "You can treat them nicely or otherwise."
    print "At the end of the game, your fate will be determined by how you acted."

    choice = raw_input("Would you like to play a game? (y)upe, (n)ope? ")

    if choice == "y":
        print "Great! Please use 'm' for mean and 'n' for nice. Let's begin."
        begin()

    if choice == "n":
        print "I understand... No... I don't understand... Why did you run the game then?"
        exit()

    elif choice != "y"+"n":
        bad_lang()
        
def begin():
    global nice
    global mean

    if nice > 2:
        print "You are a nice person, you win life!"
        choice = raw_input("Would you like to try again? (y)upe, (n)ope? ")

        if choice == "y"+"Y":
            print "Awesome... Giddy-up!"
            nice = 0
            mean = 0
            begin()

        if choice == "n"+"N":
            print "OkayILoveYouBuByeeee!!!!"
            exit()

        elif choice != "y"+"n"+"Y"+"N":
            bad_lang()

    if mean > 2:
        print "Ya big meanie! Have some worms..."
        print ">>> G-A-M-E O-V-E-R <<<"
        choice = raw_input("Want to give it another try? (y)upe, (n)ope? ")

        if choice == "y"+"Y":
            print "Better luck this time..."
            nice = 0
            mean = 0
            begin()

        if choice == "n"+"N":
            print "You! Off my planet! Enjoy them worms..."
            exit()

        elif choice != "y"+"n"+"Y"+"N":
            bad_lang()

    pick = raw_input("A stranger approaches you on the street. Will you be nice or mean? (n)ice, (m)ean? ")

    if pick == "n":
        print "They smile, wave and walk away."
        nice = nice+1
        print "You currently have " +str(nice) + " points of good karma."
        begin()

    if pick == "m":
        print "The stranger frowns, gives you the bird, and storm off!"
        mean = mean+1
        print "You currently have " +str(mean) + " points of bad juju."
        begin()

start()
