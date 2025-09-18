import sys

if len(sys.argv) == 1:
    print("none")
else:
    x = len(sys.argv)-1
    print(f"parameters: {x}")

    for i in sys.argv[1:]:
        lenge = len(i)
        print(i, " : ",lenge)