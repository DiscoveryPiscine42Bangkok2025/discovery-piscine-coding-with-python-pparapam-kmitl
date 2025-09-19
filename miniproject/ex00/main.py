from checkmate import checkmate

def main():
    board = """\
..Q.
.K..
....
....\
"""
    checkmate(board)  # ควรได้ "Success"

if __name__ == "__main__":
    main()
