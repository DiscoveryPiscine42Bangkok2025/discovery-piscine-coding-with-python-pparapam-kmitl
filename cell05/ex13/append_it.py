import sys

if len(sys.argv) == 1:
    print("none")
else:
    for para in sys.argv[1:]:
        if para.endswith("ism"):
            continue
        else:
            print(para + "ism")