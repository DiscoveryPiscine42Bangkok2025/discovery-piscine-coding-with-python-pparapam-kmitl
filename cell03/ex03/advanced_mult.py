i = 0

while i <= 10:
    print("Table de", i,": ", end=" ")

    j = 0
    while j <= 10:
        result = i * j
        print(result, end=" ")
        j += 1
    
    print()
    
    i += 1