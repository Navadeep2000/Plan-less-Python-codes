#A function to count all the characters present in the input string including special characters and spaces
def CHARACTER_COUNT(String):
    return len(String)


# A function to count the number of words present in the input string
def WORD_COUNT(String):
    words = String.split(' ')  # Split function with a space character splits the input string at space character
    return len(words)
    # Assumption1 - EACH CONSECUTIVE WORD IS SEPARATED BY A SPACE CHARACTER
    # Assumption2 - WHEN SENTENCE ENDS WITH A '.' OR ANY OTHER PUNCTUATIONS, A SPACE IS GIVEN WHILE STARTING NEXT WORD


# Main function
sentence = input("Enter sentence(s) to begin Count :  ")
print("Number of characters             : ", CHARACTER_COUNT(sentence))
print("Number of words in the sentence  : ", WORD_COUNT(sentence))
