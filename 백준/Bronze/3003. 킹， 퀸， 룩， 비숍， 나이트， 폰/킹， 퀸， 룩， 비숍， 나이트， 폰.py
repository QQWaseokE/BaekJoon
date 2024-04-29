def chess(a):
    chess_list = a.split()

    chess_list[0] = str(1 - int(chess_list[0]))
    chess_list[1] = str(1 - int(chess_list[1]))
    chess_list[2] = str(2 - int(chess_list[2]))
    chess_list[3] = str(2 - int(chess_list[3]))
    chess_list[4] = str(2 - int(chess_list[4]))
    chess_list[5] = str(8 - int(chess_list[5]))

    result = " ".join(chess_list)

    print(result)


chess_number = input()
chess(chess_number)
