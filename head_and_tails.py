import random

input("Press enter to see if the result is head of tails ")
result = random.randint(1,2)
if result == 1:
    print("Head")
    input("Press enter to leave ")
else:
    print("Tails")
    input("Press enter to leave ")