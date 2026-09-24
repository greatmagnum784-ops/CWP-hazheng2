
import sys

if len(sys.argv) != 2:
    print("none")
else:
    passed_param = sys.argv[1]
    try:

        user_input = input("What was the parameter? ")

        if user_input == passed_param:
            print("Good job!")
        else:
            print("Nope, sorry...")
    except (EOFError, KeyboardInterrupt):
        pass