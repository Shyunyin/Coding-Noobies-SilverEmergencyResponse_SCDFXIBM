#detect keywords in the responses
#if else statements and elif for the 3 situations

code_yellow = int(0)
code_orange = int(0)
response1 = input("If you are conscious please move any part of your body or say yes: ")
if response1 in ['yes', 'i can talk', 'i am conscious', "i can move"]:
    response2 = input("\nHave you fallen: ")
    if response2 in ['no', 'i am okay', 'i am fine', "it's okay", 'i have gotten up', 'i got up', 'yes, but i have gotten up']:
        print("Description = 'Code-Zero'")
    else:
        code_yellow = int(code_yellow + 1)
        code_orange = int(code_orange + 1)
        response3 = input("\nAre you bleeding: ")
        if response3 == "No":
            code_yellow = int(code_yellow + 1)
        else:
            code_orange = int(code_orange + 1)
        response4 = input("\nCan you tell me where you are feeling pain: ")
        if response4 in ['head', 'hip', 'back']:
            code_orange = int(code_orange + 1)
        else:
            code_yellow = int(code_yellow + 1)
        response5 = input("\nDo you remember how you fell: ")
        if response5 in ['yes', 'slipped', 'slippery floor', 'tripped on something','wet', 'dizzy', 'faint', 'no strength']:
            code_yellow = int(code_yellow + 1)
        else:
            code_orange = int(code_orange + 1)
        response6 = input("\nAre you able to move your body: ")
        if response6 in ['Can', 'Abit', 'Can stand up', 'Can move', 'Yes']:
            code_yellow = int(code_yellow + 1)
        else:
            code_orange = int(code_orange + 1)
        response7 = input("\nAre you on any medication that makes you drowsy now: ")
        if response7 in ['no']:
            code_yellow = int(code_yellow + 1)
        else:
            code_orange = int(code_orange + 1)
        response8 = input("\nWhat is the year currently: ")
        if response8 in ['twenty twenty', 'two thousand and twenty', 'two thousand twenty', 'two zero two zero', '2020']:
            code_yellow = int(code_yellow + 1)
        else:
            code_orange = int(code_orange + 1)
            
        if int(code_yellow) > int(code_orange):
            print ("\nDescription = Code-Yellow")
        elif int(code_yellow) < int(code_orange):
            print ("\nDescription = Code-Orange")
else:
    print("Description = Code-Red")
        

        



