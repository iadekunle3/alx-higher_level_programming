#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]  # Exclude the script name itself
    num_args = len(args)

    if num_args == 0:
        print("{} arguments.".format(num_args))
    else:
        print("{} argument{}:".format(num_args, 's' if num_args > 1 else ''))
        print('\n'.join("{}: {}".format(i, arg) for i, arg in enumerate(args, start=1)))

