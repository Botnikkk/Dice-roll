import asyncio
import random
        
async def dice_roll() :
    print(32*"=" ,"DICE ROLL" , 32*"=" )
    dice_top = "\n" + " "*24 +  " ________    "*2 + "\n" + " "*24+   "|        |   "*2
    dice_mid =   "\n" + " "*24 +  "|   {num}    |   ".format(num = random.randint(1,6)) + "|   {num}    |".format(num = random.randint(1,6)) + "\n"
    dice_bottom =   " "*24 + "|________|   "*2 + "\n" 
    dices = dice_top + dice_mid + dice_bottom
    await asyncio.sleep(1)
    print("\nRolling in.....")
    for i in range(1,4) : 
        await asyncio.sleep(1)
        print(4-i)
    await asyncio.sleep(1)
    print(dices)
    print("="*75)
    
asyncio.run(dice_roll())
answer = input("\n\nRoll again?\n* Yes\n* No\n- ").lower()
if answer in ["yes", "no"] :
    while answer == "yes" :
        asyncio.run(dice_roll()) 
        answer = input("\n\nRoll again?\n* Yes\n* No\n- ").lower()
else : 
    while answer not in ["yes", "no"] :
        print("That is not a valid answer")
        answer = input("\n\nRoll again?\n* Yes\n* No\n- ").lower()
    while answer == "yes" :
       asyncio.run(dice_roll()) 
