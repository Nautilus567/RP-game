import random
import time


def roll_dice(diceType, force):
    """

    Function to simulate a roll dice, takes the type of the dice, form 4 to 20
    and takes the force applying to the dice from 1 to 10, the code
    represent the "force" by iterating

    Takes: Dice type(int) and force (int)
    Returns: Result form the roll (int)
    :type force: int
    :type diceType: int

    """
    for times in range(force):
        roll = random.randint(1, diceType)
    if force == 1:
        print('You gently drop the dice')
        time.sleep(2)
    elif force == 10:
        print('You launch the dice with all your forces')
        time.sleep(2)
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


def effect(score, threshold, diceType):
    """
    Helper function that indicates the actual effect of the dice into the player action
    :type diceType:int
    :param diceType: Max number capable from dice
    :param score: Int, result from roll_dice
    :param threshold: Int, minimal score to accomplish the action
    :return: string, indicates if the result is a critical hit, critical failure, failure, success or in the limit
    """
    if score == 1:
        # Critical Failure
        return 'CritFail'
    elif 1 < score < threshold:
        # Under requirements
        return 'Fail'
    elif score == threshold:
        # On Limit
        return 'Limit'
    elif score == diceType:
        # Critical Hit
        return 'CritHit'
    else:
        return 'Success'

