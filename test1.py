import json
import difflib
import pprint
from difflib import get_close_matches
from termcolor import colored


data=json.load(open("data.json"))
w="hi"
def print_g(d):
    a="a"
    for i in d:
        print("  "+str(a)+"."+colored(i,"blue"))
        a =chr(ord(a)+1)
        
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif(get_close_matches(w,data.keys()) != []):
         guess = get_close_matches(w,data.keys())[0]
         yn = input("Did you mean %s? \nEnter Y for yes and N for no:" %guess)
         if yn == "Y":
             return data[guess]
         else:
             return " "
    else:
        return "The word does'nt exist.Please double check it"


while(w != "EXIT"):
     w=input(colored("Enter the word:","green"))
     #print(colored(translate(w),"blue"))
     print_g(translate(w))
# input('Press ENTER to exit')