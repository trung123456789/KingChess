from Board import Board

btn_list = []
btn_miss_list = []
init_table_chess = [["" for i in range(8)] for j in range(8)]
init_board = Board(btn_list, init_table_chess, btn_miss_list)
init_board.init_start_game()
