def evaluateString(input):
    """This function evaluates an arithmetic expression represented as a
    string containing only positive integers and the addition (+) operator."""
    # base case, if there are no more + operators in the expression
    if "+" not in input:
        return int(input)

    # Split the string at the first '+' operator into two parts
    first_number, remaining_input = input.split('+', 1)

    # recursively repeat the above split until we are down to our base case of
    # just one number remaining, then go back up adding all the numbers together
    return evaluateString(remaining_input) + int(first_number)