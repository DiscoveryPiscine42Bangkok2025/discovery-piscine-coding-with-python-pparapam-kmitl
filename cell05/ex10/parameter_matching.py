import sys

if len(sys.argv) !=2 :
    print("none")
else :
    user = input("What was the parameter? ")
    x = sys.argv[1]
    if user == x:
        print("Good job!")
    else:
        print("Nope, sorry...")