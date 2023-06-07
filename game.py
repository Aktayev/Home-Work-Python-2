import random
x=0
while True:
    try:
        y = int(input("level: "))
        if y < 0:
            print("Please, enter a positive integer.")
        else:
            break
    except ValueError:
        pass
m = random.randint(x,y)
print(f"Right answer is:{m}")
while True:
    try:
        n = int(input("Guess: "))
        if n > m:
            print("Too large!")
        elif n < 0:
            print("Please, enter a positive integer.")
        elif n < m:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        print("Please, enter a positive integer.")
        pass
