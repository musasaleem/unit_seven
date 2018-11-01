def code():
    print("You will chose to decode encode or quit any code of your choosing")
    option = input("decode, encode or quit?")
    if option in ["encode", "e", "encoded"]:
        print("you chose to encode")
        return "e"
    if option in ["decode", "d"]:
        print("you chose to decode")
        return "d"
    else:
        return "q"


def main():

    if code() == "e":
        number = int(input("choose any number between 0-24"))
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        first = alphabet[number:]
        last = alphabet[0: number]
        final = first + last
        encoded = ""
        phrase = input("choose any phrase you want to encode")
        for x in phrase:
            if x == " ":
                encoded = encoded + " "
            else:
                bet = alphabet.index(x)
                end = final[bet]
                encoded = encoded + end
        print(encoded)

    elif code() == "d":
        number = int(input("choose any number between 0-24"))
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        last = alphabet[number:]
        first = alphabet[0: number]
        final = first + last
        decoded = ""
        phrase = input("choose any phrase you want to encode")
        for x in phrase:
            if x == " ":
                decoded = decoded + " "
            else:
                bet = alphabet.index(x)
                end = final[bet]
                decoded = decoded + end
        print(decoded)


            #number = int(input("choose any number between 0-24"))
            #alphabet = "abcdefghijklmnopqrstuvwxyz"
          #first = alphabet[number + 1:]
           # last = alphabet[0: number]
           # final =  last + first
           # print(final)


main()  #while code():
        #while True:0000i