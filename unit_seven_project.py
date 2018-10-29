def code():
    print("You will chose to decode encode or quit any code of your choosing")
    option = int(input("decode, encode or quit?"))
    if option in ["encode", "e"]:
        print("you chose to encode")
        return True
    if option in ["decode", "d"]:
        return
    else:
        return False

def main():
            phrase = input("choose any phrase you want to encode")
            number = int(input("choose any number between 0-24"))
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            first = alphabet[number:]
            last = alphabet[0: number]
            final = first + last
            final_word = []
            final_word = phrase.index(1)
            print(final)



            #number = int(input("choose any number between 0-24"))
            #alphabet = "abcdefghijklmnopqrstuvwxyz"
            #first = alphabet[number + 1:]
           # last = alphabet[0: number]
           # final =  last + first
           # print(final)


main()  #while code():
        #while True: