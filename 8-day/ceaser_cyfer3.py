from ceazer_cyfer_part1 import alphabet
from ceazer_cyfer_part2 import text,shift,direction

def ceazer(msg,direction,shift):
    indexes = []
    cyfer = ''
    for c in msg:
        indexes.append(alphabet.index(c))
    if direction == "decode":
        for i in indexes:
            cyfer += alphabet[i-shift]
    elif direction == "encode":
        for i in indexes:
            if i+shift > (len(alphabet)-1):
                cyfer += alphabet[(i+shift )- len(alphabet)]
            else:
                cyfer += alphabet[i+shift]
    print(f"the {direction} message is {cyfer} ")
    


ceazer(msg=text,shift=shift,direction=direction)