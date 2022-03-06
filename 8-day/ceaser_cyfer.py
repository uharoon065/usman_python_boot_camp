from pdb import set_trace

### the video solution  is in while loop where you just have to use modules operator instead of while loop to get a shift number which is not greater the length of list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceazer(msg,direction,shift):
    cyfer = ''
    # while shift > len(alphabet):
        # shift = shift -len(alphabet)
    if direction == "decode":
        shift = -shift
    for c in msg:
        if c in alphabet:
            position = alphabet.index(c) + shift
            if position > (len(alphabet)-1):
                position= position - len(alphabet)
            cyfer += alphabet[position]
        else:
            cyfer += c
    print(f"the {direction} message is {cyfer} ")

is_end_coding_and_decoding = False
while not is_end_coding_and_decoding:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    ceazer(msg=text,shift=shift,direction=direction)
    isContinue = input("do you want to continue ? yes or no ").lower()
    if isContinue == "no":
        is_end_coding_and_decoding = True
        print("good bye")
    