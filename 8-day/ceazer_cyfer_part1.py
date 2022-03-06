# import pdb
# pdb.set_trace()
'''

step 1 i have to itterate over the  text so i can find the position of each character in the list
then for my eassy  im storing all the positions in a list called indexes
now i am itterating over the indexes list and adding the shift  which will  give me a shifted character which im concating to variable called cyfer
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(txt,shift):
    cyfer = ''
    indexes = []
    for c in txt:
        indexes.append(alphabet.index(c))

    for i in indexes:
        if i+shift > (len(alphabet)-1):
            cyfer += alphabet[(i+shift )- len(alphabet)]
        else:
            cyfer += alphabet[i+shift]

    print(f"the encoded message is {cyfer} ")



    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# encrypt(txt = text,shift = shift)