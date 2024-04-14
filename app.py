from random import randint

DICE_TYPES = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def dice_roll(input):
    for dice in DICE_TYPES:
        if dice in input:
            try:
                multiply, modifier = input.split(dice)
            except ValueError:
                return "Wrong input!"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong input!"

    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong input!"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong input!"

    return sum([randint(1, dice_value) for _ in range(multiply)]) + modifier


if __name__ == "__main__":
    print(dice_roll("2D10+10"))
    print(dice_roll("D6"))
    print(dice_roll("D2D3"))
    print(dice_roll("D12-1"))
    print(dice_roll("DD34"))
    print(dice_roll("4-3D6"))
