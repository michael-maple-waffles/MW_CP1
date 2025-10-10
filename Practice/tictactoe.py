board = [1,2,3,4,5,6,7,8,9]
while True:
    yn = input("would you like to play? (Y/N)").strip().
    if yn == "Y":
        while True:
            print(f"{board(0)}|{board(1)}|{board(2)}\n-----\n{board(3)}|{board(4)}|{board(5)}\n-----\n{board(6)}|{board(7)}|{board(8)}")
    elif yn == "N":
        break
    else:
        print("make sure this is a Y or a N")
