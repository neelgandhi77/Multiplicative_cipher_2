character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Multiplicative_encrypt(Plaintext, key):
    Plaintext=''.join(Plaintext.split())
    Plaintext=Plaintext.lower()
    outText = []
    cryptText = []
    for eachLetter in Plaintext:
        if eachLetter in character:
            # index letters 
            index = character.index(eachLetter)
            # C = (P * K) mod 26
            crypting = (index * key) % 26
            cryptText.append(crypting)
            newLetter = character[crypting]
            outText.append(newLetter)
    temp=''.join(map(str,outText))
    return temp.upper()


# function modular multiplicative inverse
def modInverse(key, numchar) :
  for x in range(1, numchar) :
    if (((key % numchar) * (x%numchar)) % numchar == 1) :
      return x
  #y = pow(key, -1, numchar)
  return -1
  '''
    if ((key * x) % numchar == 1) :
      return x
  #y = pow(key, -1, numchar)
  return 1
  '''

def Multiplicative_decrypt(ciphertext,mI, key):
  outText = []
  decryptText = []
  ciphertext=''.join(ciphertext.split())
  ciphertext=ciphertext.lower()
  if(mI==-1):
    outText="!!! GCD(Key,26)!=1 "
  else:
    for eachLetter in ciphertext:
        if eachLetter in character:
        # index letters
        index = character.index(eachLetter)
        # C = (P * K^-1) mod 26
        decrypt = (index * mI ) % 26
        #print(modInverse(key, 26))
        decryptText.append(decrypt)
        newLetter = character[decrypt]
        outText.append(newLetter)
  #print(mI)   
  
  temp=''.join(map(str,outText))
  return temp


'''
text = input ('Type text to Decrypt: ')
ciphertext = str(text)
num = input('Type key between 0-25: ')
key = int(num)
mI=modInverse(key, 26)
print('Plain Text:' ,*Multiplicative_decrypt(ciphertext,mI, key))



text = input ('Type text to encrypt: ')
plaintext = str(text)
num = input('Type key between 0-25: ')
key = int(num)
print('Ciphertext:' ,*Multiplicative_encrypt(plaintext, key)) 
'''
