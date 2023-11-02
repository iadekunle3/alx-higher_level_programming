#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    ops = {'+': add, '-': sub, '*': mul, '/': div}

    if op in ops:
        print("{} {} {} = {}".format(a, op, b, opsop))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

