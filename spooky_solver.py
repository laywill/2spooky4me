#!/usr/bin/env python3.11

import sys
import re
import copy
import operator


# Alias functions from Operator Library based on valid input operator symbols
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
    "^": operator.pow,
}


def operate(arbitrary_string: str, operator: str, operator_value: int) -> str:
    # Create a list of integers, splitting on strings made only of non-digits
    numbers = re.split(r"\D+", arbitrary_string)
    numbers = list(filter(None, numbers))
    numbers = list(map(int, numbers))
    
    # Create a list of words, splitting on strings made only of digits
    words = re.split(r"\d+", arbitrary_string)
    words = list(filter(None, words))

    # Create a list of numbers that have been operated on
    operated_on_numbers = copy.deepcopy(numbers)
    if len(numbers):
        for idx, num in enumerate(numbers):
            if operator not in OPERATORS.keys():
                raise KeyError(f"Unexpected operator '{operator}', please use one of: +, -, *, /, ^")
            # Convert the operator string to a function reference
            operator_func = OPERATORS[operator]
            # Apply the function to the inputs
            operated_on_numbers[idx] = operator_func(num, operator_value)
    
    # Prepare an output string to populate
    output_str = ""
    
    # Zip fails if either list is empty.
    # If only one list contains something, return that.
    if not len(numbers):
        output_str = words[0]
    elif not len(words):
        output_str = str(operated_on_numbers[0])
    else:
        # Need to make sure we recombine in the right order
        # Check first character of the arbitrary string to see if it was a word or number.
        if arbitrary_string[0] in "0123456789":
            output_str = "".join([x for z in zip(list(map(str, operated_on_numbers)), words) for x in z])
        else:
            output_str = "".join([x for z in zip(words, list(map(str, operated_on_numbers))) for x in z])
    return output_str


def _get_operator(input_string: str) -> str:
    operator =  str(input_string[0])
    if operator not in "+-*/^":
        raise ValueError(f"Unexpected operator '{operator}', please use one of: +, -, *, /, ^")
    return operator


def _get_operator_value(input_string: str) -> int:
    return int(input_string[1:])


def main(arguments: list) -> str:
    arbitrary_string = arguments[1].strip()
    operator = _get_operator(arguments[2])
    operator_value = _get_operator_value(arguments[2])

    output = operate(arbitrary_string, operator, operator_value)
    print(output)
    return output


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise IndexError("Not enough arguments passed in.")
    main(sys.argv)
