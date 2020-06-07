from math import inf as infinity


def getNum(message: str, minimum: int = -infinity, maximum: int = infinity, default: int = None):
    """
    Static method to receive sanitised input from the user, with error checking and only returns once a valid
    number is given
    :param message: Text to be displayed to the user, prompting an integer input
    :param minimum: Minimum value of user's integer number input
    :param maximum: Maximum value of user's integer number input
    :param default: Default value of user's integer number input
    :return: Integer constrained to given parameters
    """

    # If minimum and maximum are accidentally wrong, swap
    if minimum and maximum and maximum < minimum:
        temp = maximum
        maximum = minimum
        minimum = temp

    minText = ""
    if minimum != -infinity:
        minText = f" (minimum: {minimum})"

    maxText = ""
    if maximum != infinity:
        maxText = f" (maximum: {maximum})"

    defaultText = ""
    if default:
        defaultText = f" (default: {default})"

    while True:
        inputNum = input(f"{message}{minText}{maxText}{defaultText}: ")

        if inputNum == "":
            if default:
                return default
            else:
                print("Enter a number")

        try:
            inputNum = int(inputNum)
            if maximum >= inputNum >= minimum:
                return inputNum
            else:
                print(f"Enter a number within the given range")
        except ValueError:
            print("Enter a valid number")


def getChoice(message: str, choices: list, numInsteadOfText: bool = False, sort: bool = False):
    """
    Static method that takes sanitised user input to decide on one of the choices given in the choices list
    :param message: Text to be displayed to the user, prompting an choice
    :param choices: List of choices that the user must select one of (list of strings)
    :param numInsteadOfText: If true, return the index of the choice (1st, 2nd, ... in the choices list)
    :param sort: Sort the items before requesting a choice from the user
    :return: # Returns either the choice number or the choice string itself, dependent on numInsteadOfText parameter
    """

    # Get distinct lowercase choices from choices
    choices = list(dict.fromkeys([choice.lower() for choice in choices]).keys())

    if sort:
        choices.sort()

    # For each choice, create a choice num that the user can use to choose
    for choiceNum in (choiceRange := range(1, len(choices) + 1)):
        print(f"{choiceNum}. {choices[choiceNum - 1].capitalize()}")
    print()

    while True:
        choice = input(f"{message}: ")

        if choice.lower() in choices:
            if numInsteadOfText:
                return choices.index(choice)
            else:
                return choice

        if choice.isdigit():
            if (choiceNum := int(choice)) in choiceRange:
                if numInsteadOfText:
                    return choiceNum
                else:
                    return choices[choiceNum - 1]
