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

            number = int(input("choose any number between 0-24"))
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            first = alphabet[number:]
            last = alphabet[0: number]
            final = first + last
            phrase = input("choose any phrase you want to encode")
            for x in phrase:
                code = phrase.index(x)
                end = final[code]
                print(end)


            #number = int(input("choose any number between 0-24"))
            #alphabet = "abcdefghijklmnopqrstuvwxyz"
0            #first = alphabet[number + 1:]
           # last = alphabet[0: number]
           # final =  last + first
           # print(final)


main()  #while code():
        #while True:0000