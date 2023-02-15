#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    names = invited_names.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letters:
    letters = starting_letters.readlines()
    print(letters)

def new_letter(name):
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as ready_to_send:
        x = letters[0].replace("[name]", name)
        ready_to_send.write(x)
        for t in range(1, len(letters)):
            ready_to_send.write(letters[t])

for name in names:
    x = name.strip()
    new_letter(x)

