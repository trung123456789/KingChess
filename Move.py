from PIL import ImageTk, Image
import constant
import tkinter.messagebox


class Move:
    def __init__(self, init_table_chess, btn_list, old_button, btn_miss_list, init_miss_chess, lbl_mis, session_player,
                 session_img):
        self.init_table_chess = init_table_chess
        self.btn_list = btn_list
        self.old_button = old_button
        self.btn_miss_list = btn_miss_list
        self.init_miss_chess = init_miss_chess
        self.not_chess = ImageTk.PhotoImage(Image.open("not_chess.png"))
        self.lbl_mis = lbl_mis
        self.session_player = session_player
        self.session_img = session_img
        self.img_white = ImageTk.PhotoImage(Image.open("white.jpg"))
        self.add_queen = ImageTk.PhotoImage(Image.open("add_queen.png"))

    def btn_click_piece(self, buttons, play):
        if play == constant.PvM:
            print(play)
        else:
            print(play)
        if buttons['bg'] == 'yellow':
            print(len(self.lbl_mis))
            print(self.lbl_mis[10]['text'])
            print(self.lbl_mis[11]['text'])

            name_chess = self.old_button['text'].split('-')[0]
            x_old = self.old_button['text'].split('-')[1]
            y_old = self.old_button['text'].split('-')[2]
            x = buttons['text'].split('-')[1]
            y = buttons['text'].split('-')[2]
            str_temp = name_chess + '-' + x + '-' + y
            str_temp_old = '-' + x_old + '-' + y_old

            self.handle_session(x, name_chess)

            self.init_table_chess[int(x_old)][int(y_old)] = ''
            self.init_table_chess[int(x)][int(y)] = name_chess

            # Add chess missing to show
            self.handle_chess_miss(buttons)

            buttons['text'] = str_temp
            buttons['image'] = self.old_button['image']

            self.old_button.config(image=self.not_chess)
            self.old_button.config(text=str_temp_old)

            # Handle finish game
            self.default_board()
            if self.finish_game() == constant.WHITE_KING_CHESS or self.finish_game() == constant.BLACK_KING_CHESS:
                self.disable_board()
                if self.finish_game() == constant.WHITE_KING_CHESS:
                    tkinter.messagebox.showinfo(constant.KING_CHESS_TITLE, constant.WHITE_CHESS_WIN)
                else:
                    tkinter.messagebox.showinfo(constant.KING_CHESS_TITLE, constant.BLACK_CHESS_WIN)

            self.old_button = buttons
        else:
            self.default_board()
            if buttons['text'].split('-')[0] != '':
                if self.handle_play_with_session(buttons):
                    return
            if buttons['text'].split('-') != '':
                values = buttons['text'].split('-')
                name_chess = values[0]
                x = values[1]
                y = values[2]
                self.draw_road(name_chess, x, y)
                if self.session_player != constant.SESSION_ADD_QUEEN:
                    self.old_button = buttons

    def handle_session(self, x, name_chess):
        if x == str(7) and name_chess == constant.P_W_CHESS:
            flg_have_chess = 0
            for i in range(len(self.btn_miss_list)):
                if i % 2 == 0 and len(self.btn_miss_list[i]['text'].split('-')[0].split('.')) == 3:
                    flg_have_chess = 1
                    break
            if flg_have_chess == 1:
                self.enable_miss_board(constant.P_W_CHESS)
                self.session_player = constant.SESSION_ADD_QUEEN
                self.lbl_mis[11].config(image=self.img_white)
                self.lbl_mis[10].config(image=self.add_queen)
        if x == str(0) and name_chess == constant.P_B_CHESS:
            flg_have_chess = 0
            for i in range(len(self.btn_miss_list)):
                if i % 2 != 0 and len(self.btn_miss_list[i]['text'].split('-')[0].split('.')) == 3:
                    flg_have_chess = 1
                    break
            if flg_have_chess == 1:
                self.enable_miss_board(constant.P_B_CHESS)
                self.session_player = constant.SESSION_ADD_QUEEN
                self.lbl_mis[10].config(image=self.img_white)
                self.lbl_mis[11].config(image=self.add_queen)

        if self.session_player == constant.SESSION_PLAYER_1:
            self.session_player = constant.SESSION_PLAYER_2
            self.lbl_mis[11].config(image=self.session_img)
            self.lbl_mis[10].config(image=self.img_white)
        elif self.session_player == constant.SESSION_PLAYER_2:
            self.session_player = constant.SESSION_PLAYER_1
            self.lbl_mis[10].config(image=self.session_img)
            self.lbl_mis[11].config(image=self.img_white)

    def handle_chess_miss(self, buttons):
        for i in range(len(self.btn_miss_list)):
            if buttons['text'].split('-')[0] != '':
                if buttons['text'].split('-')[0].split('.')[1] == 'W':
                    if self.btn_miss_list[i]['text'].split('-')[0] == buttons['text'].split('-')[0] + '.M':
                        self.lbl_mis[i]['text'] = str(int(self.lbl_mis[i]['text']) + 1)
                        break
                    if self.btn_miss_list[i]['text'].split('-')[0] == 'W':
                        self.btn_miss_list[i]['image'] = buttons['image']
                        name_old = buttons['text'].split('-')[0].split('.')[0]
                        name = self.btn_miss_list[i]['text'].split('-')[0]
                        x = self.btn_miss_list[i]['text'].split('-')[1]
                        y = self.btn_miss_list[i]['text'].split('-')[2]
                        self.btn_miss_list[i]['text'] = name_old + '.' + name + '.M' + '-' + x + '-' + y
                        self.lbl_mis[i]['text'] = '1'
                        break
                if buttons['text'].split('-')[0].split('.')[1] == 'B':
                    if self.btn_miss_list[i]['text'].split('-')[0] == buttons['text'].split('-')[0] + '.M':
                        self.lbl_mis[i]['text'] = str(int(self.lbl_mis[i]['text']) + 1)
                        break
                    if self.btn_miss_list[i]['text'].split('-')[0] == 'B':
                        self.btn_miss_list[i]['image'] = buttons['image']
                        name_old = buttons['text'].split('-')[0].split('.')[0]
                        name = self.btn_miss_list[i]['text'].split('-')[0]
                        x = self.btn_miss_list[i]['text'].split('-')[1]
                        y = self.btn_miss_list[i]['text'].split('-')[2]
                        self.btn_miss_list[i]['text'] = name_old + '.' + name + '.M' + '-' + x + '-' + y
                        self.lbl_mis[i]['text'] = '1'
                        break

    def handle_play_with_session(self, buttons):
        if self.session_player == constant.SESSION_PLAYER_1:
            if buttons['text'].split('-')[0].split('.')[1] == 'B':
                return True
        elif self.session_player == constant.SESSION_PLAYER_2:
            if buttons['text'].split('-')[0].split('.')[1] == 'W':
                return True
        else:
            if len(buttons['text'].split('-')[0].split('.')) == 3:
                if buttons['text'].split('-')[0].split('.')[2] == 'M':
                    temp = self.old_button['image']
                    self.old_button['image'] = buttons['image']

                    name_1 = self.old_button['text'].split('-')[0].split('.')[0]
                    name_2 = self.old_button['text'].split('-')[0].split('.')[1]
                    for i in range(len(self.btn_miss_list)):
                        if len(self.btn_miss_list[i]['text'].split('-')[0].split('.')) == 3:
                            print(self.btn_miss_list[i]['text'])
                            name_m_1 = self.btn_miss_list[i]['text'].split('-')[0].split('.')[0]
                            name_m_2 = self.btn_miss_list[i]['text'].split('-')[0].split('.')[1]
                            if name_m_1 == name_1 and name_m_2 == name_2:
                                self.lbl_mis[i]['text'] = str(int(self.lbl_mis[i]['text']) + 1)
                                break
                        else:
                            if self.btn_miss_list[i]['text'].split('-')[0] == buttons['text'].split('-')[0].split('.')[1]:
                                self.lbl_mis[i]['text'] = '1'
                                buttons['image'] = temp
                                break
                    name_old_miss = self.old_button['text'].split('-')[0]
                    x_old = self.old_button['text'].split('-')[1]
                    y_old = self.old_button['text'].split('-')[2]

                    name_curr_1 = buttons['text'].split('-')[0].split('.')[0]
                    name_curr_2 = buttons['text'].split('-')[0].split('.')[1]
                    name_chess_add = name_curr_1 + '.' + name_curr_2
                    str_temp_old = name_chess_add + '-' + x_old + '-' + y_old
                    self.init_table_chess[int(x_old)][int(y_old)] = str_temp_old
                    if buttons['text'].split('-')[0].split('.')[1] == 'W':
                        self.session_player = constant.SESSION_PLAYER_2
                        self.lbl_mis[11].config(image=self.session_img)
                        self.lbl_mis[10].config(image=self.img_white)
                    else:
                        self.session_player = constant.SESSION_PLAYER_1
                        self.lbl_mis[10].config(image=self.session_img)
                        self.lbl_mis[11].config(image=self.img_white)

                    self.disable_miss_board()
                    self.old_button['text'] = str_temp_old
                    buttons['text'] = name_old_miss + '.M' + '-' + x_old + '-' + y_old
            return True

    def draw_road(self, name_chess, x, y):
        pos_list = []
        if name_chess == 'P.W':
            pos_list = self.draw_road_pawn(name_chess, int(x), int(y), pos_list)
        if name_chess == 'P.B':
            pos_list = self.draw_road_pawn(name_chess, int(x), int(y), pos_list)
        if name_chess == 'Q.W' or name_chess == 'Q.B':
            pos_list = self.draw_road_queen(int(x), int(y), pos_list)
        if name_chess == 'R.W' or name_chess == 'R.B':
            pos_list = self.draw_road_rook(int(x), int(y), pos_list)
        if name_chess == 'B.W' or name_chess == 'B.B':
            pos_list = self.draw_road_boship(int(x), int(y), pos_list)
        if name_chess == 'H.W' or name_chess == 'H.B':
            pos_list = self.draw_road_horse(int(x), int(y), pos_list)
        if name_chess == 'K.W' or name_chess == 'K.B':
            pos_list = self.draw_road_king(int(x), int(y), pos_list)
        print(pos_list)
        for i in range(len(self.btn_list)):
            for j in range(len(pos_list)):
                str_pos = '-' + str(pos_list[j][0]) + '-' + str(pos_list[j][1])
                if name_chess.split('.')[1] == 'W':
                    name_temp = self.btn_list[i]['text'].split('-')[0]
                    x_temp = self.btn_list[i]['text'].split('-')[1]
                    y_temp = self.btn_list[i]['text'].split('-')[2]
                    str_temp = '-' + x_temp + '-' + y_temp
                    if str_temp == str_pos:
                        if name_temp != '':
                            print(name_temp.split('.'))
                            if 'B' in name_temp.split('.')[1]:
                                self.btn_list[i].config(bg='yellow')
                        else:
                            self.btn_list[i].config(bg='yellow')
                else:
                    name_temp = self.btn_list[i]['text'].split('-')[0]
                    x_temp = self.btn_list[i]['text'].split('-')[1]
                    y_temp = self.btn_list[i]['text'].split('-')[2]
                    str_temp = '-' + x_temp + '-' + y_temp
                    if str_temp == str_pos:
                        if name_temp != '':
                            print(name_temp.split('.'))
                            if 'W' in name_temp.split('.')[1]:
                                self.btn_list[i].config(bg='yellow')
                        else:
                            self.btn_list[i].config(bg='yellow')

    def draw_road_pawn(self, name_chess, x, y, pos_list):
        if name_chess == 'P.W':
            if x + 1 <= 7:
                if self.init_table_chess[x + 1][y] == '':
                    pos_list.append([x + 1, y])
                if y >= 1 and self.init_table_chess[x + 1][y-1] != '':
                    pos_list.append([x + 1, y-1])
                if y <= 6 and self.init_table_chess[x + 1][y+1] != '':
                    pos_list.append([x + 1, y+1])
            if x == 1:
                if x + 2 <= 7:
                    if self.init_table_chess[x+1][y] == '' and self.init_table_chess[x+2][y] == '':
                        pos_list.append([x + 2, y])
        else:
            if x - 1 >= 0:
                if self.init_table_chess[x - 1][y] == '':
                    pos_list.append([x - 1, y])
                if y >= 1 and self.init_table_chess[x - 1][y-1] != '':
                    pos_list.append([x - 1, y-1])
                if y <= 6 and self.init_table_chess[x - 1][y+1] != '':
                    pos_list.append([x - 1, y+1])
            if x == 6:
                if x - 2 >= 0:
                    if self.init_table_chess[x-1][y] == '' and self.init_table_chess[x-2][y] == '':
                            pos_list.append([x - 2, y])
        return pos_list

    def draw_road_queen(self, x, y, pos_list):
        pos_list = self.draw_road_rook(x, y, pos_list)
        pos_list = self.draw_road_boship(x, y, pos_list)
        return pos_list

    def draw_road_rook(self, x, y, pos_list):
        flag = 0
        for i in range(x-1, -1, -1):
            if flag == 0:
                if self.init_table_chess[i][y] == '':
                    pos_list.append([i, y])
                if self.init_table_chess[i][y] != '':
                    pos_list.append([i, y])
                    break

        flag = 0
        for i in range(x+1, 8):
            if flag == 0:
                if self.init_table_chess[i][y] == '':
                    pos_list.append([i, y])
                if self.init_table_chess[i][y] != '':
                    pos_list.append([i, y])
                    break

        flag = 0
        for i in range(y-1, -1, -1):
            if flag == 0:
                if self.init_table_chess[x][i] == '':
                    pos_list.append([x, i])
                if self.init_table_chess[x][i] != '':
                    pos_list.append([x, i])
                    break

        flag = 0
        for i in range(y+1, 8):
            if flag == 0:
                if self.init_table_chess[x][i] == '':
                    pos_list.append([x, i])
                if self.init_table_chess[x][i] != '':
                    pos_list.append([x, i])
                    break
        return pos_list

    def draw_road_boship(self, x, y, pos_list):
        flag_c = 0
        i_temp = y-1
        for i in range(x-1, -1, -1):
            if flag_c == 0:
                if i_temp < 0:
                    continue
                if self.init_table_chess[i][i_temp] == '':
                    pos_list.append([i, i_temp])
                if self.init_table_chess[i][i_temp] != '':
                    pos_list.append([i, i_temp])
                    flag_c = 1
            if flag_c == 1:
                break
            i_temp -= 1
        flag_c = 0
        i_temp = y+1
        for i in range(x - 1, -1, -1):
            if i_temp > 7:
                break
            if flag_c == 0:
                if self.init_table_chess[i][i_temp] == '':
                    pos_list.append([i, i_temp])
                if self.init_table_chess[i][i_temp] != '':
                    pos_list.append([i, i_temp])
                    flag_c = 1
            if flag_c == 1:
                break
            i_temp += 1

        flag_c = 0
        i_temp = y-1
        for i in range(x+1, 8):
            if flag_c == 0:
                if i_temp < 0:
                    continue
                if self.init_table_chess[i][i_temp] == '':
                    pos_list.append([i, i_temp])
                if self.init_table_chess[i][i_temp] != '':
                    pos_list.append([i, i_temp])
                    flag_c = 1
            if flag_c == 1:
                break
            i_temp -= 1

        flag_c = 0
        i_temp = y+1
        for i in range(x+1, 8):
            if i_temp > 7:
                break
            if flag_c == 0:
                if self.init_table_chess[i][i_temp] == '':
                    pos_list.append([i, i_temp])
                if self.init_table_chess[i][i_temp] != '':
                    pos_list.append([i, i_temp])
                    flag_c = 1
            if flag_c == 1 or i_temp == 7:
                break
            i_temp += 1

        return pos_list

    def draw_road_horse(self, x, y, pos_list):
        for i in range(x-2, x + 3):
            for j in range(y-2, y + 3):
                if i >= 0 and j >= 0 and i <= 7 and j <= 7:
                    if i == x-2 and j == y - 1:
                        pos_list.append([i, j])
                    if i == x - 2 and j == y + 1:
                        pos_list.append([i, j])
                    if i == x - 1 and j == y - 2:
                        pos_list.append([i, j])
                    if i == x - 1 and j == y + 2:
                        pos_list.append([i, j])
                    if i == x + 1 and j == y - 2:
                        pos_list.append([i, j])
                    if i == x + 1 and j == y + 2:
                        pos_list.append([i, j])
                    if i == x + 2 and j == y + 1:
                        pos_list.append([i, j])
                    if i == x + 2 and j == y - 1:
                        pos_list.append([i, j])
        return pos_list

    def draw_road_king(self, x, y, pos_list):
        for i in range(x-1, x + 2):
            for j in range(y-1, y + 2):
                if i >= 0 and j >= 0 and i <= 7 and j <= 7:
                    if i != x or j != y:
                        pos_list.append([i, j])
        return pos_list

    def default_board(self):
        idx = 0
        for i in range(3, 11):
            for j in range(0, 8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.btn_list[idx].config(bg='white')
                    else:
                        self.btn_list[idx].config(bg='#BDC8D8')
                elif i % 2 != 0:
                    if j % 2 == 0:
                        self.btn_list[idx].config(bg='#BDC8D8')
                    else:
                        self.btn_list[idx].config(bg='white')
                idx += 1

    def finish_game(self):
        w_flg = constant.WHITE_KING_CHESS
        b_flg = constant.BLACK_KING_CHESS
        for i in range(len(self.init_table_chess)):
            for j in range(len(self.init_table_chess)):
                if self.init_table_chess[i][j] == constant.K_B_CHESS:
                    w_flg = ''
                if self.init_table_chess[i][j] == constant.K_W_CHESS:
                    b_flg = ''
        if w_flg == '' and b_flg == '':
            return constant.CONTINUE_GAME
        if w_flg != '':
            return w_flg
        if b_flg != '':
            return b_flg

    def disable_board(self):
        for i in range(len(self.btn_list)):
            self.btn_list[i].config(state='disabled')

    def enable_miss_board(self, c):
        for i in range(len(self.btn_miss_list)):
            if c == constant.P_W_CHESS and i % 2 == 0:
                self.btn_miss_list[i].config(state='normal')
            if c == constant.P_B_CHESS and i % 2 != 0:
                self.btn_miss_list[i].config(state='normal')

    def disable_miss_board(self):
        for i in range(len(self.btn_miss_list)):
            self.btn_miss_list[i].config(state='disabled')
