import requests
import json

#Api key for the meriam-webster api
api_key = ""

#Function that sends a request to the api and gets the short definitions of a chosen word
def lookup():
    word_to_lookup = str(input("Word: "))
    #Requests information about the chosen word
    definition_to_find = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word_to_lookup}?key={api_key}")
    response = definition_to_find.json()
    
    #Checks if the json response of the api request is empty, if it is: the word is not valid and no other word can be suggested
    if len(response) == 0:
        print("Word Not Recognized!")
    else:
=
        #Checks if the response is an array filled with suggested spellings
        if str(response[0]).count(" ") == 0:
            #Print a list of suggested words to lookup
            for j in range(len(response)):
                print(str(j + 1) + ". " + response[j])
            print()
            #Ask the user which word they want to lookup up from the suggestions
            correction_word = int(input("Did you mean any of these words below? (enter corresponding number): "))
            #If the user selects an invalid number, print the error and quit the program
            if correction_word <= 0 or correction_word >= (len(response) + 1):
                print("Invalid Number!")
                quit()
            #Requests information about the new chosen word
            print("Word: " + str(response[correction_word - 1]))
            definition_to_find = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{response[correction_word - 1]}?key={api_key}")
            response = definition_to_find.json()
        #Number the short definitions for clarity
        definition_number = 1
        for definition in response[0]['shortdef']:
            print(str(definition_number) +". " + definition)
            definition_number += 1

#Run the lookup function
lookup()
#The choice to lookup another word is initially set to false
another_word_lookup = True
while another_word_lookup == True:
    #Blank space for clarity
    print()
    #Ask the user if they want to lookup another word
    another_word_lookup_choice = input("Do you want to lookup another word? (y/n): ")
    if another_word_lookup_choice == "y":
        #Run the lookup function again
        lookup()
    else:
        #Set the choice to lookup another word to false, so the while loop breaks
        another_word_lookup = False
    
