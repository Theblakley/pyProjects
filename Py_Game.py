#
# Python: 3.8.1
#
# Author: Andrew M. Blakley
#
# Purpose: The Tech Academy - Python Course, Creating our first program together. 
#          Demonstrating how to pass variables from function to function
#          while producing a functional game.  
#
#          Remember, function_name(variable) _means that we pass in the variable. 
#          return variable_means that we are returning the variable to  
#          back to the calling function.



def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank the player
        for plaing again and continue with the game
    """
    # meaning, if we do not already have this user's name.
    # then they are a new player and we need to get their name
    if name !="":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \m>>> ").capitalize()
                if name !="":
                    print("\nWelcome, {}".format(name))
                    print("\nIn this game, you will be greeted \nby several dfferent people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop=false
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ".lower()
        if pick =="n":
            print("\nThe stranger walks away smiling....")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off....")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()
                     


if __name__ == "__main__":
        start()
