import random
import turtle
from turtle import *


# Drawing of circles
def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
# Drawing of rectangles
def draw_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.setheading(0)
    

# Number of tries set to 0
trys = 0

# List of word for computer to pick from
words_list = [
    "above",
    "actor",
    "adopt",
    "black",
    "brain",
    "bread",
    "chief",
    "clean",
    "class"]

# The secret word
secret_word = "#####"


# Setting up the turtle window
speed(0)
turtle.setup(600, 600)
window = turtle.Screen()
window.bgcolor("#FFFFFF")

# Creating the game
def display_game(draw_backgrd=True, draw_bottom=True, draw_mid=True, draw_top=True, welcome=True,
                 button1=False, button2=False, button3=False, lefty=False, righty=False, draw_le=False, draw_re=False,
                 draw_mouth=False, draw_nose=False, ask=True):

    if draw_backgrd == True:
        draw_circle(turtle, "cyan", 0, -200, 220)

    if draw_bottom == True:
        draw_circle(turtle, "white", 0, -180, 90)

    if draw_mid == True:
        draw_circle(turtle, "white", 0, -60, 70)

    if draw_top == True:
        draw_circle(turtle, "white", 0, 50, 50)
        hideturtle()

    if welcome == True:
        penup()
        color("pink")
        goto(-110, 250)
        write("Snow-Man Game", font=("Arial", 20, "bold"))

    if button1 == True:
        draw_circle(turtle, "black", 0, -80, 7)
        hideturtle()

    if button2 == True:
        draw_circle(turtle, "black", 0, -35, 7)
        hideturtle()

    if button3 == True:
        draw_circle(turtle, "black", 0, 10, 7)
        hideturtle()

    if lefty == True:
        left(45)
        draw_rectangle(turtle, "brown", 50, 25, 50, 5)
        left(0)
        draw_rectangle(turtle, "brown", 75, 50, 20, 3)
        left(90)
        draw_rectangle(turtle, "brown", 75, 50, 20, 3)
        hideturtle()

    if righty == True:
        right(45)
        draw_rectangle(turtle, "brown", -90, 55, 50, 5)
        left(0)
        draw_rectangle(turtle, "brown", -100, 45, 20, 3)
        left(90)
        draw_rectangle(turtle, "brown", -75, 45, 20, 3)
        hideturtle()

    if draw_le == True:
        draw_circle(turtle, "black", -15, 110, 7)
        hideturtle()

    if draw_re == True:
        draw_circle(turtle, "black", 15, 110, 7)
        hideturtle()

    if draw_mouth == True:
        draw_circle(turtle, "red", 0, 80, 12)
        draw_circle(turtle, "white", 0, 85, 12)
        hideturtle()

    if draw_nose == True:
        draw_circle(turtle, "orange", 0, 98, 5)
        hideturtle()

    if ask == True:
        askGameType()

    return True

# Drawing of the 3 buttons of Snow-man
def buttons(button1=True, button2=True, button3=True):

    if button1==True:
        draw_circle(turtle, "black", 0, -80, 7)
        hideturtle()

    if button2==True:
        draw_circle(turtle, "black", 0, -35, 7)
        hideturtle()

    if button3==True:
        draw_circle(turtle, "black", 0, 10, 7)
        hideturtle()

    return True

# Drawing of Snow-man hands
def hands(lefty=True, righty=True ):

    if lefty == True:
        left(45)
        draw_rectangle(turtle, "brown", 50, 25, 50, 5)
        left(0)
        draw_rectangle(turtle, "brown", 75, 50, 20, 3)
        left(90)
        draw_rectangle(turtle, "brown", 75, 50, 20, 3)
        hideturtle()

    if righty == True:
        right(45)
        draw_rectangle(turtle, "brown", -90, 55, 50, 5)
        left(0)
        draw_rectangle(turtle, "brown", -100, 45, 20, 3)
        left(90)
        draw_rectangle(turtle, "brown", -75, 45, 20, 3)
        hideturtle()

    return True

# Drawing of Snow-man eyes
def eyes(draw_le=True, draw_re =True):

    if draw_le == True:
        draw_circle(turtle, "black", -15, 110, 7)
        hideturtle()

    if draw_re == True:
        draw_circle(turtle, "black", 15, 110, 7)
        hideturtle()  

    return True

# Drawing of Snow-man mouth
def mouth(draw_mouth=True):

    if draw_mouth == True:
        draw_circle(turtle, "red", 0, 80, 12)
        draw_circle(turtle, "white", 0, 85, 12)
        hideturtle()

    return True

# Drawing of snow-man nose
def nose(draw_nose=True):

    if draw_nose == True:
        draw_circle(turtle, "orange", 0, 98, 5)
        hideturtle()

    return True


# hidding of secrewor with the '#' symbol
def dashed(secret_word):

    unguessed_letters = ["#" for el in secret_word]
    unguessed_letters_str = str(unguessed_letters)
    dashes = unguessed_letters_str.replace('[', "").replace(',', "").replace("]", "").replace("'", "").replace(" ", "")

    return dashes

no_correct_guesses = dashed(secret_word)

# function for input letters
def input_letters(one=False, two=False, three=False, four=False, five=False):
    letter=""
    if one==True:
        letter = textinput("Guess the first letter", no_correct_guesses)
        return letter
    if two==True:
        letter = textinput("Correct! Make your second guess", first_guessed_letter)
        return letter
    if three==True:
        letter = textinput("Good! Guess the third letter", second_guessed_letter)
        return letter
    if four==True:
        letter = textinput("Great! Now the fourth guess", third_guessed_letter)
        return letter
    if five==True:
        letter = textinput("Fantastic! Make your last guess", fourth_guessed_letter)

    return letter
    

letter = input_letters()

# Function for number of guessed letters
def one_guessed(no_correct_guesses, letter):
    
    #i = 0
    if letter == secret_word[0]:      
        show_first = no_correct_guesses[0].replace("#", letter)
        return show_first

first_guessed_letter = one_guessed(no_correct_guesses, letter)

def two_guessed(first_guessed_letter, letter):
    
    if letter == secret_word[1]:
        show_second = first_guessed_letter[1].replace("#", letter)
        return show_second

second_guessed_letter = two_guessed(first_guessed_letter, letter)

def three_guessed(second_guessed_letter, letter):
    
    if letter == secret_word[2]:             
        show_third = second_guessed_letter[2].replace("#", letter)
        return show_third

third_guessed_letter = three_guessed(second_guessed_letter, letter)

def four_guessed(third_guessed_letter, letter):
    
    if letter == secret_word[3]:             
        show_fourth = third_guessed_letter[3].replace("#", letter)
        return show_fourth

fourth_guessed_letter = four_guessed(third_guessed_letter, letter)

def five_guessed(fourth_guessed_letter, letter):
    
    if letter == secret_word[4]:             
        show_fifth = fourth_guessed_letter[4].replace("#", letter)
        return show_fifth

fifth_guessed_letter = five_guessed(fourth_guessed_letter, letter)

# Functions to allow for guesses
def first_guess(secret_word, trys, no_correct_guesses, first_guessed_letter):

    letter = input_letters(one=True, two=False, three=False, four=False, five=False)
    
    if letter == secret_word[0] and len(letter) == 1:

        penup()
        color("lime")
        goto(-80, -290)
        write(letter, font=("Arial", 50, "bold"))

        trys += 1
        return second_guess(secret_word, trys, first_guessed_letter, second_guessed_letter)
    elif len(letter) != 1:
        trys += 1
        textinput("One letter at a time.", "Hit Enter And Try Again.")
        return first_guess(secret_word, trys, no_correct_guesses, first_guessed_letter)
    else:
        trys += 1
        textinput("Wrong!", "Hit Enter And Try Again.")
        return first_guess(secret_word, trys, no_correct_guesses, first_guessed_letter)


    return True


def second_guess(secret_word, trys, first_guessed_letter, second_guessed_letter):

    buttons()
    letter = input_letters(one=False, two=True, three=False, four=False, five=False)

    if letter == secret_word[1] and len(letter) == 1:

        penup()
        color("lime")
        goto(-40, -290)
        write(letter, font=("Arial", 50, "bold"))

        trys += 1
        return third_guess(secret_word, trys, second_guessed_letter, third_guessed_letter)
    elif len(letter) != 1:
        trys += 1
        textinput("One letter at a time.", "Hit Enter And Try Again.")
        return second_guess(secret_word, trys, first_guessed_letter, second_guessed_letter)
    else:
        trys += 1
        textinput("Wrong!", "Hit Enter And Try Again.")
        return second_guess(secret_word, trys, first_guessed_letter, second_guessed_letter)


    return True

def third_guess(secret_word, trys, second_guessed_letter, third_guessed_letter):
    

    hands()
    letter = input_letters(one=False, two=False, three=True, four=False, five=False)

    if letter == secret_word[2] and len(letter) == 1:

        penup()
        color("lime")
        goto(0, -290)
        write(letter, font=("Arial", 50, "bold"))

        trys += 1
        return fourth_guess(secret_word, trys, third_guessed_letter, fourth_guessed_letter)
    elif len(letter) != 1:
        trys += 1
        textinput("One letter at a time.", "Hit Enter And Try Again.")
        return third_guess(secret_word, trys, second_guessed_letter, third_guessed_letter)
    else:
        trys += 1
        textinput("Wrong!", "Hit Enter And Try Again.")
        return third_guess(secret_word, trys, second_guessed_letter, third_guessed_letter)


    return True

def fourth_guess(secret_word, trys, third_guessed_letter, fourth_guessed_letter):
    
    eyes()
    letter = input_letters(one=False, two=False, three=False, four=True, five=False)


    if letter == secret_word[3] and len(letter) == 1:

        penup()
        color("lime")
        goto(40, -290)
        write(letter, font=("Arial", 50, "bold"))

        trys += 1
        return fifth_guess(secret_word, trys, fourth_guessed_letter, fifth_guessed_letter)
    elif len(letter) != 1:
        trys += 1
        textinput("One letter at a time.", "Hit Enter And Try Again.")
        return fourth_guess(secret_word, trys, third_guessed_letter, fourth_guessed_letter)
    else:
        trys += 1
        textinput("Wrong!", "Hit Enter And Try Again.")
        return fourth_guess(secret_word, trys, third_guessed_letter, fourth_guessed_letter)

    return True

def fifth_guess(secret_word, trys, fourth_guessed_letter, fifth_guessed_letter):
    
    mouth()
    letter = input_letters(one=False, two=False, three=False, four=False, five=True)

    if letter == secret_word[4] and len(letter) == 1:

        penup()
        color("lime")
        goto(80, -290)
        write(letter, font=("Arial", 50, "bold"))

        trys += 1
        return completed(trys)
    elif len(letter) != 1:
        trys += 1
        textinput("One letter at a time.", "Hit Enter And Try Again.")
        return fifth_guess(secret_word, trys, fourth_guessed_letter, fifth_guessed_letter)
    else:
        trys += 1
        textinput("Wrong!", "Hit Enter And Try Again.")
        return fifth_guess(secret_word, trys, fourth_guessed_letter, fifth_guessed_letter)


    return True

def completed(trys):

    nose()
    trys_str = str(trys)

    penup()
    color("purple")
    goto(-100, 180)
    write("Congratulations", font=("Arial", 20, "bold"))

    penup()
    color("yellow")
    goto(-72, 150)
    write("After " + trys_str + " trys", font=("Arial", 20, "bold"))

    enter = textinput("Do you wanna play again?", "1) Yes \n2) No")
    
    if enter == "1" or enter.casefold() == "yes".casefold():
        speed(0)
        clear()
        display_game()
    elif enter == "2" or enter.casefold() == "no".casefold():
        exit()   

    else:
        textinput("Not A Valid Input", "Try again!")
        speed(0)
        clear()        
        display_game()
    return True

# Asking Computer to pick word
def askComputerToPick():
    global secret_word
    secret_word = random.choice(words_list)
    return secret_word.lower()


# Asking Host to pick word
def askHostToTypeSecretWord(repeatText=None):
    question = repeatText if repeatText is not None else "Type in your secret 5-letter word or 'exit' enter 'back' for Menu.\n"
    global secret_word
    secret_word = textinput("SECRET WORD!", question)

    if type(secret_word) == str and len(secret_word) == 5:
        return secret_word.lower()
    elif secret_word == 'back':
        return askGameType()
    elif secret_word == "exit":
        exit()
    else:
        return askHostToTypeSecretWord("Please the word should be exactly 5 letters! Type again or 'back' for Main Menu.\n")

# Asking for game mode
def askGameType():
    question = "Please choose"
    option = "1) One Player Mode\n2) Two Player Mode\n3) 'exit'\n"
    game_type = textinput(question, option)
    if type(game_type) == str and game_type == "1":
        secret_word = askComputerToPick()
        first_guess(secret_word, trys, no_correct_guesses, first_guessed_letter)
        return secret_word

    elif type(game_type) == str and game_type == "2":
        secret_word = askHostToTypeSecretWord()
        first_guess(secret_word, trys, no_correct_guesses, first_guessed_letter)
        return secret_word

    elif game_type == "exit" or game_type == "3":
        exit()

    else:
        return askGameType()

    return True

# initializing the game
display_game()

window.listen()
exitonclick()

