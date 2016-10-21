import random
import time


def roll_dice(diceType, force):
    """

    Function to simulate a roll dice, takes the type of the dice, form 4 to 20
    and takes the force applying to the dice from 1 to 10, the code
    represent the "force" by iterating

    Takes: Dice type(int) and force (int)
    Returns: Result form the roll (int)
    """
    for times in range(force):
        roll = random.randint(1, diceType)
    if force == 1:
        print('You gently drop the dice')
        time.sleep(1)
    elif force == 10:
        print('You launch the dice with all your forces')
        time.sleep(5)
    elif 1 < force < 5:
        print('You throw the dice like a professional gambler')
        time.sleep(2)
    elif force == 5:
        print('You throw the dice making it bounce happily')
        time.sleep(2)
    else:
        print('You throw the dice hitting the board with a spin')
        time.sleep(2)
    return roll
