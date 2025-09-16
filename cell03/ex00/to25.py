user_num = int(input("User Number: "))

if user_num > 25:
    print("Error")
else :
    for i in range(user_num, 26) :
        print("Inside the loop, my variable is ", i)