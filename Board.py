from tkinter import *
import random
from PIL import ImageTk, Image
from Move import Move
import constant


class Board:
    tk = Tk()
    tk.title = "King Chess"
    cv_start_game = Canvas(tk)
    cv_start_game.grid(row=1, column=0)

    def __init__(self, btn_list, init_table_chess, btn_miss_list):
        self.session_player = constant.SESSION_PLAYER_1
        self.btn_list = btn_list
        self.init_table_chess = init_table_chess
        self.btn_miss_list = btn_miss_list
        self.lbl_miss = []
        self.init_miss_chess = [["" for i in range(5)] for j in range(2)]
        self.flag_click = 0
        self.old_button = 0

        self.flg_play = 'PvM'
        self.radio_list = []

        self.img_white = ImageTk.PhotoImage(Image.open("white.jpg"))
        self.img_black = ImageTk.PhotoImage(Image.open("black.jpg"))
        self.img_start = ImageTk.PhotoImage(Image.open("start.png"))
        self.img_reset = ImageTk.PhotoImage(Image.open("reset.png"))
        self.img_finish = ImageTk.PhotoImage(Image.open("finish.png"))

        self.king_b = ImageTk.PhotoImage(Image.open("king_b.png"))
        self.king_w = ImageTk.PhotoImage(Image.open("king_w.png"))
        self.queen_b = ImageTk.PhotoImage(Image.open("queen_b.png"))
        self.queen_w = ImageTk.PhotoImage(Image.open("queen_w.png"))
        self.bishop_b = ImageTk.PhotoImage(Image.open("bishop_b.png"))
        self.bishop_w = ImageTk.PhotoImage(Image.open("bishop_w.png"))
        self.rook_b = ImageTk.PhotoImage(Image.open("rook_b.png"))
        self.rook_w = ImageTk.PhotoImage(Image.open("rook_w.png"))
        self.horse_b = ImageTk.PhotoImage(Image.open("horse_b.png"))
        self.horse_w = ImageTk.PhotoImage(Image.open("horse_w.png"))
        self.pawn_b = ImageTk.PhotoImage(Image.open("pawn_b.png"))
        self.pawn_w = ImageTk.PhotoImage(Image.open("pawn_w.png"))
        self.session_img = ImageTk.PhotoImage(Image.open("session_player.png"))

        self.move = Move(init_table_chess, btn_list, self.old_button, self.btn_miss_list, self.init_miss_chess,
                         self.lbl_miss, self.session_player, self.session_img)

    def init_start_game(self):
        def show_choice(v):
            self.flg_play = v

        radio_pvm = Radiobutton(self.cv_start_game, font='Times 12 bold', text='Player vs Machine', value='PvM',
                                fg='green', command=lambda: show_choice(constant.PvM))
        radio_pvm.grid(row=1, column=0)
        radio_pvp = Radiobutton(self.cv_start_game, font='Times 12 bold', text='Player1 vs Player2', value='PvP',
                                fg='green', command=lambda: show_choice(constant.PvP))
        radio_pvp.grid(row=2, column=0)
        self.radio_list.append(radio_pvp)
        self.radio_list.append(radio_pvm)

        lbl_start = Label(self.cv_start_game, text="Start Game", font='Times 14 bold', fg='green',
                          height=1, width=10)
        lbl_start.grid(row=1, column=1)
        button_start = Button(self.cv_start_game, image=self.img_start,
                              height=constant.HEIGHT_BTN, width=constant.WIDTH_BTN,
                              command=lambda: self.start_game(button_start, lbl_start))
        button_start.grid(row=2, column=1)

        lbl_end = Label(self.cv_start_game, text="End Game", font='Times 14 bold', fg='red', height=1, width=10)
        button_end = Button(self.cv_start_game, image=self.img_finish, height=constant.HEIGHT_BTN,
                            width=constant.WIDTH_BTN, command=lambda: self.end_game())
        lbl_end.grid(row=1, column=2)
        button_end.grid(row=2, column=2)
        self.tk.mainloop()

    def start_game(self, button_start, lbl_start):
        lbl_start.config(fg='gray')
        button_start.config(image=self.img_start, state=DISABLED)
        button_reset = Button(self.cv_start_game, image=self.img_reset,
                              height=constant.HEIGHT_BTN, width=constant.WIDTH_BTN,
                              command=lambda: self.restart_game())
        lbl_reset = Label(self.cv_start_game, text="Restart Game", font='Times 14 bold', fg='blue', height=1, width=10)
        lbl_reset.grid(row=1, column=1)
        button_reset.grid(row=2, column=1)

        self.init_board()
        self.miss_chess_piece()
        self.disable_miss_board()
        self.disable_radio()

    def end_game(self):
        self.tk.destroy()

    def restart_game(self):
        self.enable_board()
        self.disable_miss_board()
        self.session_player = constant.SESSION_PLAYER_1
        self.set_default_board()
        self.disable_radio()
        flag = 0
        for i in range(len(self.init_table_chess)):
            for j in range(len(self.init_table_chess)):
                str_temp = '-' + str(i) + '-' + str(j)
                self.btn_list[flag].config(text=str_temp, image=self.img_white)
                self.init_table_chess[i][j] = ''
                if i == 0:
                    if j == 0 or j == 7:
                        self.btn_list[flag].config(image=self.rook_w, text=constant.R_W_CHESS + str_temp)
                        self.init_table_chess[i][j] = constant.R_W_CHESS
                    if j == 1 or j == 6:
                        self.btn_list[flag].config(image=self.horse_w, text=constant.H_W_CHESS + str_temp)
                        self.init_table_chess[i][j] = constant.H_W_CHESS
                    if j == 2 or j == 5:
                        self.btn_list[flag].config(image=self.bishop_w, text=constant.B_W_CHESS + str_temp)
                        self.init_table_chess[i][j] = constant.B_W_CHESS
                    if j == 3:
                        self.btn_list[flag].config(image=self.queen_w, text=constant.Q_W_CHESS + str_temp)
                        self.init_table_chess[i][j] = constant.Q_W_CHESS
                    if j == 4:
                        self.btn_list[flag].config(image=self.king_w, text=constant.K_W_CHESS + str_temp)
                        self.init_table_chess[i][j] = constant.K_W_CHESS
                if i == 7:
                    if j == 0 or j == 7:
                        self.btn_list[flag].config(image=self.rook_b, text=constant.R_B_CHESS + str_temp)
                        self.init_table_chess[i][j] = constant.R_B_CHESS
                    if j == 1 or j == 6:
                        self.btn_list[flag].config(image=self.horse_b, text=constant.H_B_CHESS + str_temp)
                        self.init_table_chess[i][j] = constant.H_B_CHESS
                    if j == 2 or j == 5:
                        self.btn_list[flag].config(image=self.bishop_b, text=constant.B_B_CHESS + str_temp)
                        self.init_table_chess[i][j] = constant.B_B_CHESS
                    if j == 3:
                        self.btn_list[flag].config(image=self.queen_b, text=constant.Q_B_CHESS + str_temp)
                        self.init_table_chess[i][j] = constant.Q_B_CHESS
                    if j == 4:
                        self.btn_list[flag].config(image=self.king_b, text=constant.K_B_CHESS + str_temp)
                        self.init_table_chess[i][j] = constant.K_B_CHESS
                if i == 1:
                    self.btn_list[flag].config(image=self.pawn_w, text=constant.P_W_CHESS + str_temp)
                    self.init_table_chess[i][j] = constant.P_W_CHESS
                elif i == 6:
                    self.btn_list[flag].config(image=self.pawn_b, text=constant.P_B_CHESS + str_temp)
                    self.init_table_chess[i][j] = constant.P_B_CHESS
                flag += 1

        for i in range(len(self.btn_miss_list)):
                if i % 2 == 0:
                    str_temp = 'W-' + str(i) + '-' + str(j)
                else:
                    str_temp = 'B-' + str(i) + '-' + str(j)

                self.btn_miss_list[i].config(image=self.img_white, text=str_temp)
                self.lbl_miss[i].config(text='0')

    def init_board(self):
        text = 1
        canvas_board = Canvas(self.tk)
        canvas_board.grid(row=2, column=0)
        for i in range(3, 11):
            for j in range(0, 8):
                str_temp = '-' + str(i-3) + '-' + str(j)
                button = Button(canvas_board, state=NORMAL, image=self.img_white,
                                width=constant.WIDTH_CHESS, height=constant.HEIGHT_CHESS)
                if i % 2 == 0:
                    if j % 2 == 0:
                        button.config(bg='white', text=str_temp)
                    else:
                        button.config(bg='#BDC8D8', text=str_temp)
                elif i % 2 != 0:
                    if j % 2 == 0:
                        button.config(bg='#BDC8D8', text=str_temp)
                    else:
                        button.config(bg='white', text=str_temp)
                if i == 3:
                    if j == 0 or j == 7:
                        button.config(image=self.rook_w, text=constant.R_W_CHESS + str_temp)
                        self.init_table_chess[i-3][j] = constant.R_W_CHESS
                    if j == 1 or j == 6:
                        button.config(image=self.horse_w, text=constant.H_W_CHESS + str_temp)
                        self.init_table_chess[i-3][j] = constant.H_W_CHESS
                    if j == 2 or j == 5:
                        button.config(image=self.bishop_w, text=constant.B_W_CHESS + str_temp)
                        self.init_table_chess[i-3][j] = constant.B_W_CHESS
                    if j == 3:
                        button.config(image=self.queen_w, text=constant.Q_W_CHESS + str_temp)
                        self.init_table_chess[i-3][j] = constant.Q_W_CHESS
                    if j == 4:
                        button.config(image=self.king_w, text=constant.K_W_CHESS + str_temp)
                        self.init_table_chess[i-3][j] = constant.K_W_CHESS
                if i == 10:
                    if j == 0 or j == 7:
                        button.config(image=self.rook_b, text=constant.R_B_CHESS + str_temp)
                        self.init_table_chess[i-3][j] = constant.R_B_CHESS
                    if j == 1 or j == 6:
                        button.config(image=self.horse_b, text=constant.H_B_CHESS + str_temp)
                        self.init_table_chess[i-3][j] = constant.H_B_CHESS
                    if j == 2 or j == 5:
                        button.config(image=self.bishop_b, text=constant.B_B_CHESS + str_temp)
                        self.init_table_chess[i-3][j] = constant.B_B_CHESS
                    if j == 3:
                        button.config(image=self.queen_b, text=constant.Q_B_CHESS + str_temp)
                        self.init_table_chess[i-3][j] = constant.Q_B_CHESS
                    if j == 4:
                        button.config(image=self.king_b, text=constant.K_B_CHESS + str_temp)
                        self.init_table_chess[i-3][j] = constant.K_B_CHESS
                if i == 4:
                    button.config(image=self.pawn_w, text=constant.P_W_CHESS + str_temp)
                    self.init_table_chess[i-3][j] = constant.P_W_CHESS
                elif i == 9:
                    button.config(image=self.pawn_b, text=constant.P_B_CHESS + str_temp)
                    self.init_table_chess[i-3][j] = constant.P_B_CHESS

                button.grid(row=i, column=j)
                self.btn_list.append(button)
                text += 1
        for i in range(0, len(self.btn_list)):
            self.btn_list[i]['command'] = lambda c=i: self.move.btn_click_piece(self.btn_list[c], self.flg_play)

    def miss_chess_piece(self):
        canvas_miss = Canvas(self.tk)
        canvas_miss.grid(row=2, column=1)
        lbl_p1 = Label(canvas_miss, text='10', image=self.session_img, width=constant.WIDTH_CHESS, height=constant.HEIGHT_CHESS)
        lbl_p1.grid(row=2, column=0)
        lbl_p2 = Label(canvas_miss, text='11', image=self.img_white, width=constant.WIDTH_CHESS, height=constant.HEIGHT_CHESS)
        lbl_p2.grid(row=2, column=2)
        lbl_w = Label(canvas_miss, text="White", font='Times 10 bold', bg='white', fg='black',
                      width=constant.WIDTH_MISS_LABEL, height=constant.HEIGHT_MISS_LABEL)
        lbl_w.grid(row=3, column=0)
        lbl_b = Label(canvas_miss, bg='white', fg='black',
                      width=constant.WIDTH_MISS_LABEL, height=constant.HEIGHT_MISS_LABEL)
        lbl_b.grid(row=3, column=1)
        lbl_w = Label(canvas_miss, text='Black', font='Times 10 bold', bg='black', fg='white',
                      width=constant.WIDTH_MISS_LABEL, height=constant.HEIGHT_MISS_LABEL)
        lbl_w.grid(row=3, column=2)
        lbl_b = Label(canvas_miss, bg='black', fg='white',
                      width=constant.WIDTH_MISS_LABEL, height=constant.HEIGHT_MISS_LABEL)
        lbl_b.grid(row=3, column=3)
        for i in range(4, 9):
            for j in range(0, 3, 2):
                if j == 0:
                    str_temp = 'W-' + str(i) + '-' + str(j)
                else:
                    str_temp = 'B-' + str(i) + '-' + str(j)
                button = Button(canvas_miss, text=str_temp, state=NORMAL, image=self.img_white,
                                width=constant.WIDTH_CHESS, height=constant.HEIGHT_CHESS)
                button.grid(row=i, column=j)

                label = Label(canvas_miss, text='0', font='Times 14 bold', state=NORMAL,  width=4, height=1)
                label.grid(row=i, column=j+1)
                self.btn_miss_list.append(button)
                self.lbl_miss.append(label)
        for i in range(0, len(self.btn_miss_list)):
            self.btn_miss_list[i]['command'] = lambda c=i: self.move.btn_click_piece(self.btn_miss_list[c], self.flg_play)

        self.lbl_miss.append(lbl_p1)
        self.lbl_miss.append(lbl_p2)

    def enable_board(self):
        for i in range(len(self.btn_list)):
            self.btn_list[i].config(state='normal')

    def disable_miss_board(self):
        for i in range(len(self.btn_miss_list)):
            self.btn_miss_list[i].config(state='disabled')

    def set_default_board(self):
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

    def disable_radio(self):
        for i in range(len(self.radio_list)):
            self.radio_list[i]['state'] = 'disabled'

    def enable_radio(self):
        for i in range(len(self.radio_list)):
            self.radio_list[i]['state'] = 'normal'
