def checkmate(board):
    grid = [list(row) for row in board.splitlines()] #ตารางที่มัน... 
    size = len(grid) #ควางกว้างของ board 5 จุด = size

    # ตรวจสอบว่ากระดานเป็นจัตุรัส
    for row in grid:
        if len(row) != size: #ดูว่าบรรทัด 2 เท่ากับ 3 ไหม
            print("Error: Board is not square")
            return

    king_pos = []
    for r in range(size): #ไล่หาใน row ว่ามี king ไหม
        for c in range(size): #ไล่หาใน column ว่ามี king ไหม
            if grid[r][c] == "K": 
                king_pos.append((r, c)) #บอกตน.คิง
            

    if len(king_pos) == 0:
        print("Fail")
        return
    if len(king_pos) > 1:
        print("Error: More than one King")
        return

    kr, kc = king_pos[0]

    # Pawn
    for dr, dc in [(1,-1), (1,1)]: #ซ้าบล่าง ขวาล่าง
        rr, cc = kr+dr, kc+dc 
        if 0 <= rr < size and 0 <= cc < size and grid[rr][cc] == "P":
            print("Success")
            return

    # Bishop / Queen
    for dr, dc in [(-1,-1), (-1,1), (1,-1), (1,1)]: #ซ้ายบน ซ้ายล่าง ขวาบน ขวาล่าง
        rr, cc = kr, kc #
        while 0 <= rr < size and 0 <= cc < size:
            rr += dr
            cc += dc
            if rr < 0 or rr >= size or cc < 0 or cc >= size:
                break
            if grid[rr][cc] in ("B","Q"):
                print("Success")
                return
            if grid[rr][cc] != ".":
                break

    # Rook / Queen
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]: #บน ล่าง ซ้าย ขวา
        rr, cc = kr, kc
        while 0 <= rr < size and 0 <= cc < size:
            rr += dr
            cc += dc
            if rr < 0 or rr >= size or cc < 0 or cc >= size:
                break
            if grid[rr][cc] in ("R","Q"):
                print("Success")
                return
            if grid[rr][cc] != ".":
                break

    print("Fail")