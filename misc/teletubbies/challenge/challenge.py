import os
import time
import subprocess
blacklist="\" -;`\\|!@#$%^&*_-+=<>.~"
print("this is the most complete wiki about teletubbies\n")
print("what do you want to know ? ")
print("1) gender")
print("2) height")
print("3) hair")
print("4) eye color")
print("5) color")
print("6) favorite thing")
option=input("pick an option : ")
try:
    option=['gender','height','hair','eyes','color','favorite_thing'][int(option)-1]
except:
    print("hacker detected : go away :(")

print("\ngreat!\n")
print("1) Po")
print("2) Dipsy")
print("3) Laa-Laa")
print("4) Tinky Winky")
id=input("now pick a teletubby : ")
if any(m in id for m in blacklist):
        print("hacker detected : go away :(")
        exit()
else:  
            command = f"sqlite3 teletubbies.db \"select {option} from teletubies where id={id}\""
            result = subprocess.run(command, shell=True,stderr=subprocess.PIPE, text=True)
            error = result.stderr
            if error:
                print("an error has occured")
                print(error)
            input("\n-----------------------------------------------------\n")