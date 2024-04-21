import re

DIGIT = "[0-9]"
OPERATOR = "(\+|\-|\*|\/)"
TRANSITION_TABLE = [[1,"E","E"],[1,2,"E"],[3,"E","E"],[3,2,"A"]]
END = ""

def classify_character(character):
    if(re.match(DIGIT, character)):
        return 0, "Digit"
    elif(re.match(OPERATOR, character)):
        return 1, "Operator"
    elif(character == END):
        return 2, "END"
    else:
        print(f"Error, {character} is not valid")
        exit()

def print_header():
    print("|  Current State | Character |  Symbol  | Next State |")
    print_line()

def print_content(next_state, character, symbol, state):
    print("|      {0:2}        |     {1:1}     |  {2:<7} |    {3:2}      |".format(next_state, character, symbol, state))
    print_line()

def print_line():
    print("+" + "-" * 16 + "+" + "-" * 11 + "+" + "-" * 10 + "+" + "-" * 12 + "+")

state = 0

print("+" + "-" * 39 + "+")
print("|    Enter a string to evaluate:       |")
print("+" + "-" * 39 + "+")
string = input()
print_line()
print_header()

for character in string:
    next_state = state
    char_character, symbol = classify_character(character)
    state = TRANSITION_TABLE[state][char_character]

    if (state == "E"):
        print_content(next_state, character, symbol, state)
        print("|" + " " * 14 + "Invalid String" + " " * 25 + "|")
        print("+" + "-" * 53 + "+")
        exit()
    print_content(next_state, character, symbol, state)

if(state != 3):
    print("|" + " " * 18 + "Invalid String" + " " * 20 + "|")
    print("+" + "-" * 52 + "+")
elif(state == 3):
    print_content(state, ' ', 'END', ' ')
    print("|" + " " * 17 + "Valid String" + " " * 26 + "|")
    print("+" + "-" * 53 + "+")