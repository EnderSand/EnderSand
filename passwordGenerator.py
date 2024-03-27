import random
print("""
==================
Password Generator
==================
""")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),./?<>;':[]{}\|=+-_"

number = int(input("How many passwords would you like? "))
length = int(input("How long would you like the passwords to be? "))

wait_for_input = True

while wait_for_input == True:
  print("""Please type in a request for your password.
  The options are:
  - CAPS only
  - any combination""")
  
  request = input("Please type in one of the options: ")
  
  if request == "CAPS only":
    chars = chars[26:52]
    wait_for_input = False
    
  elif request == "any combination":
    wait_for_input = False
