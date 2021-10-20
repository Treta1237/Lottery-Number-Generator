import random

lottery = random.sample(range(1,50), 6)

while range in lottery:
    range = random.randint(1,50)

print("The lottery numbers for today are: ")
print(lottery)
