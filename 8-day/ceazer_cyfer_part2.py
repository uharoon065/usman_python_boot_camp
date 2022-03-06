from ceazer_cyfer_part1 import alphabet,encrypt
print(len(alphabet))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def decrypt(txt,shift):
  indexes = []
  cyfer = ''
  for l in txt:
    indexes.append(alphabet.index(l))
  print(indexes)
  for i in indexes:
    cyfer += alphabet[i-shift]
  print(f"the decrypted message is {cyfer} ")


# if direction == "encode":
#   encrypt(txt=text,shift=shift)
# elif direction == "decode":
#   decrypt(txt=text,shift=shift)
# else:
#   print("invalid direction")