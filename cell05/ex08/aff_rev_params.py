import sys

if len(sys.argv) < 3:
    print("none")
else :
    x = sys.argv[1:]
    for i in reversed(x):
        print(i)
