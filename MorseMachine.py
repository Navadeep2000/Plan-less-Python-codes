from pygame import mixer
import time

Morse_Set = {'A': '.-', 'B': '-...',
             'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-',
             'L': '.-..', 'M': '--', 'N': '-.',
             'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',
             'X': '-..-', 'Y': '-.--', 'Z': '--..',
             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.',
             '0': '-----',
             ',': '--..--',
             '.': '.-.-.-',
             '?': '..--..',
             '/': '-..-.',
             '-': '-....-',
             '(': '-.--.',
             ')': '-.--.-'}


def Dash():
    mixer.init()
    mixer.music.load("dash.wav")
    mixer.music.play()
    time.sleep(0.25)


def Dot():
    mixer.init()
    mixer.music.load("dot.wav")
    mixer.music.play()
    time.sleep(0.25)


def MorseEncrypt(message):
    message = message.upper()
    morse = ''  # An empty string that will be returned to the function once the ENCODED message is added to it
    for value in message:
        if value != ' ':
            morse += Morse_Set[value] + ' '  # This additional space makes 2 consecutive encoded values differ
        elif value == ' ':
            morse += '/'  # This can differentiate the morse encoded words separately
    return morse


while True:
    print("""***********************************************""")
    print("                 MORSE MACHINE                 ")
    print("""***********************************************\n""")

    string = input("Enter string to convert to Morse Audio :  ")

    code = MorseEncrypt(string)
    print("MORSE CODE for the given input      :     ", code)
    for i in code:
        if i == '-':
            Dash()
        elif i == '.':
            Dot()
        elif i == ' ':
            time.sleep(0.4)
        else:
            time.sleep(0.25)
