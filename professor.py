import random


def main():
    level = get_level()
    score = s_game(level)
    print(f"score: {score}")


def get_level():
    while True:
        try:
            level = int(input("level: "))
            if level < 4 and level > 0:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def s_round(x,y):
    count_tries = 1
    while count_tries <=3:
        try:
            answer = int(input(f"{x} + {y} =  "))
            if answer == (x + y):
                return True
            else:
                count_tries +=1
                print("EEE")
        except ValueError:
            count_tries +=1
            print(EEE)
            pass
    print(f"{x} + {y} = {x+y}")
    return False

def s_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        try:
            x, y = generate_integer(level)
            answer = s_round(x,y)
            if answer == True:
                score += 1
            count_round +=1
        except ValueError:
            pass
    return score

if __name__ == "__main__":
    main()