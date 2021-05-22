import re
import string

alphabets = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"


def encrypt(p, k):
    c = ""
    kpos = []
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in p:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x) + kpos[i]
      print(pos)
      if pos > 31:
          pos = pos-32
      c += alphabets[pos].capitalize()
      i += 1
    return c


def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in c:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x.lower()) - kpos[i]
      if pos < 0:
          pos = pos + 32
      p += alphabets[pos].lower()
      i +=1
    return p


# menu
try:
    print("Welcome to Vigenere cipher.\n\n"
          "The text message should contain only characters and the key should be one character word \n"
          "Press 1 to Encrypt a message \nPress 2 to Decrypt a message")
    choose = input("Choice: ")
    if choose == '1':
       p = input("Enter the text which you want to encrypt: ")
       p = p.replace(" ", "")
       if p.isalpha():
           k = input("Enter the key: ")
           k = k.strip()
           if k.isalpha():
               c = encrypt(p, k)
               print("The cipher text is: ", c)
           else:
               print(k)
               print("Enter valid key, key is only one character word!")
       else:
           print("Only letters are allowed!")

    elif choose == '2':
        c = input("Enter the cipher text: ")
        c = c.replace(" ", "")
        if c.isalpha():
            k = input("Enter the key: ")
            if not k.isalpha():
                print("Enter valid key, key is only one character word!")
            else:
                p = decrypt(c, k)
                print("The plain text is: ", p)
        else:
            print("Only letters are allowed!")

    else:
        print("Please enter a valid choice!")
except Exception as e:
    print(e)
    exit("Enter a valid text please! ")