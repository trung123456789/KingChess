import copy


def handle_game(init_table_chess):
    temp, _ = min_max(init_table_chess, 1, True)
    for i in range(0, len(temp)):
        for j in range(0, len(temp)):
            if temp[i][j] != init_table_chess[i][j]:
                return i, j


def check_game_over(init_table_chess):
    if check_win_horizontal(init_table_chess, "X") or check_win_vertical(init_table_chess, "X") \
            or check_win_diagonal_reverse(init_table_chess, "X") or check_win_diagonal(init_table_chess, "X"):
        return "X Win"
    if check_win_horizontal(init_table_chess, "O") or check_win_vertical(init_table_chess, "O") \
            or check_win_diagonal_reverse(init_table_chess, "O") or check_win_diagonal(init_table_chess, "O"):
        return "O Win"
    return ""


def state_list_func(table_chess, p):
    state_list = []
    for i in range(0, len(table_chess)):
        for j in range(0, len(table_chess)):
            if table_chess[i][j] == "":
                temp = copy.deepcopy(table_chess)
                temp[i][j] = p
                state_list.append(temp)
    return state_list


def check_win_horizontal(table_chess, p):
    for i in range(0, len(table_chess)):
        h = 0
        for j in range(0, len(table_chess)):
            if table_chess[i][j] == p:
                h += 1
        if h == 3:
            return True
    return False


def check_win_vertical(table_chess, p):
    for i in range(0, len(table_chess)):
        h = 0
        for j in range(0, len(table_chess)):
            if table_chess[j][i] == p:
                h += 1
        if h == 3:
            return True
    return False


def check_win_diagonal(table_chess, p):
    h = 0
    for i in range(0, len(table_chess)):
        if table_chess[i][i] == p:
            h += 1
    if h == 3:
        return True
    return False


def check_win_diagonal_reverse(table_chess, p):
    h = 0
    for i in range(0, len(table_chess)):
        if table_chess[i][len(table_chess)-i-1] == p:
            h += 1
    if h == 3:
        return True
    return False


def min_max(table_chess, depth, is_maximizing_player):
    if check_game_over(table_chess) == "X Win":
        return table_chess, 10
    if check_game_over(table_chess) == "O Win":
        return table_chess, -10
    if check_game_over(table_chess) == "" and finish_game(table_chess) == 9:
        return table_chess, 0

    if is_maximizing_player:
        best_value = -1000
        state_list_win_x = state_list_func(table_chess, "X")
        for i in range(0, len(state_list_win_x)):
            _, value = min_max(state_list_win_x[i], depth+1, False)
            if value > best_value:
                best_value = value
                state_rs = state_list_win_x[i]
        return state_rs, best_value
    else:
        best_value = 1000
        state_list_lost_o = state_list_func(table_chess, "O")

        for i in range(0, len(state_list_lost_o)):
            _, value = min_max(state_list_lost_o[i], depth+1, True)
            if value < best_value:
                best_value = value
                state_rs = state_list_lost_o[i]
        return state_rs, best_value


def finish_game(table_chess):
    flag = 0
    for i in range(0, len(table_chess)):
        for j in range(0, len(table_chess)):
            if table_chess[i][j] != "":
                flag += 1
    return flag

