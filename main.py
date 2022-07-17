import asyncio
import random

space = " "*24

def ans_check(answer) :
    if answer in ["yes", "no"] :
        return answer
    else : 
        while answer not in ["yes", "no"] :
            print("That is not a valid answer")
            answer = input("\n\nRoll again?\n* Yes\n* No\n- ").lower()
        return answer

def get_line(line) :
    return space + "|   {}    |   ".format(line[0]) + "|   {}    |".format(line[1]) + "\n"

def print_dice(print_list) :
    print("\n" + space +  " ________    "*2 )
    print(get_line(print_list[0:2]) + get_line(print_list[2:4]) + get_line(print_list[4:6]),end=" ")
    print(space +  "‾‾‾‾‾‾‾‾     "*2 + "\n")

async def dice_roll() :
    print(32*"=" ,"DICE ROLL" , 32*"=" )
    print_list = list(str(" "*6))
    print_list[2] = random.randint(1,6)
    print_list[3] = random.randint(1,6)
    await asyncio.sleep(1)
    print("\nRolling in.....")
    for i in range(1,4) : 
        await asyncio.sleep(1)
        print(4-i)
    await asyncio.sleep(1)
    print_dice(print_list)
    print("="*75)

asyncio.run(dice_roll())
answer = input("\n\nRoll again?\n* Yes\n* No\n- ").lower()
answer = ans_check(answer)
while answer == "yes" :
    asyncio.run(dice_roll())
    answer = input("\n\nRoll again?\n* Yes\n* No\n- ").lower()
    answer = ans_check(answer)
