#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

file = open("./Input/Names/invited_names.txt","r")
letters = open("./Input/Letters/starting_letter.txt",mode="r")
contents = file.readlines()
txt = letters.read()

for names in range(0,8):
    txt_name = contents[names].strip()
    x = txt.replace("[name]",txt_name)
    new_file = open(f"./Output/ReadyToSend/letter_for_{txt_name}.txt",mode="w")
    new_file.write(x)


