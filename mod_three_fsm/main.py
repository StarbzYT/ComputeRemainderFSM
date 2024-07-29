# this file is an example program to show how one may use the API
from fsm import Mod3FSM

def main():
    fsm = Mod3FSM()
    binary_integers = ["1101", "1110", "1111", "110", "1010"]
    for binary_integer in binary_integers:
        remainder = fsm.get_remainder(binary_integer)
        print(f"Remainder of {binary_integer} when divided by 3 is: {remainder}")


if __name__ == "__main__":
    main()