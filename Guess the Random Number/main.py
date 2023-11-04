import random
num = str(random.choice(range(1,4)))
res = input("En que numero pienso [1,2,3]?: ")
print("Has ganado" if res == num else "Has perdido")