import sys
import re

if len(sys.argv) != 3:
    print("none")
else :
    keyword = sys.argv[1]
    word = sys.argv[2]

    fond = re.findall(keyword, word)
    count = len(fond)
    if count == 0:
        print("none")
    else:
        print(count)