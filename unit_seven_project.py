# Musa Saleem
# Date: 11/2/18
# Last Modified: 11/2/18
# Comments: This project is about the computer using code to either encode or decode a function using caesar rotation


def code():
    """
    This is the code function where it is asking the user what they want to do, and whatever the user chooses, the
    computer puts them on a certain function
    :return: e for encode, d for decode, q for quit
    """
    print("You will chose to decode encode or quit any code of your choosing")
    option = input("decode, encode or quit?")
    if option in ["encode", "e", "encoded"]:
        print("you chose to encode")
        return "e"
    elif option in ["decode", "d"]:
        print("you chose to decode")
        return "d"
    else:
        return "q"


def main():
    choice = code()
    if choice == "e":
        number = int(input("choose any number between 0-24"))
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        first = alphabet[number:]
        last = alphabet[0: number]
        final = first + last  # changing the alphabet around to encode it
        encoded = ""  # Introducing the encoded function
        phrase = input("choose any phrase you want to encode")
        for x in phrase:
            if x == " ":
                encoded = encoded + " "  # Saying if there is a space in the phrase, keep the space and add it in rather
                # than look for it in the alphabet function
            else:
                bet = alphabet.index(x)
                end = final[bet]
                encoded = encoded + end  # Corresponding the phrase with the alphabet
        print(encoded)
    elif choice == "d":
        number = int(input("choose any number between 0-24"))
        alphabet = "zyxwvutsrqponmlkjihgfedcba"
        first = alphabet[number:]
        last = alphabet[0: number]
        final = first + last  # Changing alphabet to decode it
        decoded = ""  # Introducing decode function
        phrase = input("choose any phrase you want to decode")
        for x in phrase:
            if x == " ":
                decoded = decoded + " "  # Saying if there is a space in the phrase, keep the space and add it in rather
                # than look for it in the alphabet function
            else:
                bet = alphabet.index(x)
                end = final[bet]
                decoded = decoded + end  # Corresponding the phrase with the alphabet
        print(decoded)
    elif choice == "q":
        print("have a nice day")  # Quit function


main()
