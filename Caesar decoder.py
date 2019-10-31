#encoding: UTF-8

import getpass
#Import the python files needed for each function in the menu
import encoder
import decoder
import frecuencias

USER = getpass.getuser()
#Calls the coding function on the "encoder.py" file
def coder():
    encryptedMessage = input("Enter the message: ")
    switchIndex = int(input("Enter the switch index: "))
    output = encoder.encode(encryptedMessage, switchIndex)
    return output

#Calls the decoding function on te "decoder.py file
def deCoder():
    textInput = input("Enter the coded text: ")
    output = decoder.decoder(textInput)
    return output


def main():
    print(" ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗     ███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ ")
    print("██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗")
    print("██║     ███████║█████╗  ███████╗███████║██████╔╝    █████╗  ██╔██╗ ██║██║     ██║   ██║██║  ██║█████╗  ██████╔╝")
    print("██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██╔══╝  ██║╚██╗██║██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗")
    print("╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ███████╗██║ ╚████║╚██████╗╚██████╔╝██████╔╝███████╗██║  ██    v1.0.0" )
    print("---------------------------------------------------")
    print("Welcome %s" %USER)
    print("---------------------------------------------------")
    #Input menu
    inputMenu = int(input("Welcome to the Caesar code encoder/decoder.\n"
                      "Please enter the desired interaction on the menu:\n"
                      "1. Encoder.\n"
                      "2. Decoder.\n"
                      "0. Exit.\n"
                      "Your option: "))
    print("---------------------------------------------------")

    #While cycle: processes the value given in "inputMenu" and sends it to the according function
    while(inputMenu != 0):
        if inputMenu == 1:
            encodedMessage = coder()
            print("Encoded message: %s" % encodedMessage)
        elif inputMenu == 2:
            decodedMessage = deCoder()
            print("---------------------------------------------------\n"
                  "%s\n" #decoded message with the swamp index
                  "---------------------------------------------------" % decodedMessage)
        else:
            print("ERROR!!!! Please enter a valid value.")
            print("---------------------------------------------------")
        inputMenu = int(input("Welcome to the Caesar code encoder/decoder.\n"
                          "Please enter the desired interaction on the menu:\n"
                          "1. Encoder.\n"
                          "2. Decoder.\n"
                          "0. Exit.\n"
                          "Your option: "))
        print("---------------------------------------------------")


    print("see you soon", USER)
    print("Exiting the program...")
    print("---------------------------------------------------")


main()