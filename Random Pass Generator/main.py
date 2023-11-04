import random
import string

print("Password: ")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
chars = lower+upper+num+symbols

temp = random.sample(chars, 25)
print("".join(temp))