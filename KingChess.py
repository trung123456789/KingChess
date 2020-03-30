import random
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from HandleGame import *

tk = Tk()
tk.title("Tic Tac Toe")
btn_list = []

img_x = ImageTk.PhotoImage(Image.open("x.png"))  # PIL solution
img_o = ImageTk.PhotoImage(Image.open("o.png"))  # PIL solution
img_bg = ImageTk.PhotoImage(Image.open("white.jpg"))  # PIL solution
img_start = ImageTk.PhotoImage(Image.open("start.png"))
img_reset = ImageTk.PhotoImage(Image.open("reset.png"))
img_finish = ImageTk.PhotoImage(Image.open("finish.png"))


def init_game():
    cv_start_game = Canvas(tk)
    cv_start_game.pack()
    global lbl_think
    lbl_think = Label(cv_start_game, font='Times 10 bold', fg='red', height=1, width=16)
    lbl_think.grid(row=3, column=0)

    lbl_start = Label(cv_start_game, text="Start Game", font='Times 14 bold', fg='green', height=1, width=10)
    lbl_start.grid(row=1, column=0)
    button_start = Button(cv_start_game, image=img_start, height=40, width=150, command=lambda: start_game(cv_start_game, button_start, lbl_start))
    button_start.grid(row=2, column=0)

    lbl_end = Label(cv_start_game, text="End Game", font='Times 14 bold', fg='red', height=1, width=10)
    button_end = Button(cv_start_game, image=img_finish, height=40, width=150, command=lambda: end_game())
    lbl_end.grid(row=1, column=2)
    button_end.grid(row=2, column=2)
    tk.mainloop()


def start_game(cv_start_game, button_start, lbl_start):
    lbl_think.config(text='You are thinking...')
    lbl_start.config(fg='gray')
    button_start.config(image=img_start, state=DISABLED)
    button_reset = Button(cv_start_game, image=img_reset, height=40, width=150,
                          command=lambda: reset_game())
    lbl_reset = Label(cv_start_game, text="Restart Game", font='Times 14 bold', fg='blue', height=1, width=10)
    lbl_reset.grid(row=1, column=1)
    button_reset.grid(row=2, column=1)

    global init_table_chess
    start_player = random.randint(0, 1)
    if start_player == 0:
        init_table_chess = [["" for i in range(3)] for j in range(3)]
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        init_table_chess[x][y] = 'X'
        init_board()
        btn_list[x * 3 + y].config(image=img_x)
    else:
        init_table_chess = [["" for i in range(3)] for j in range(3)]
        init_board()


def reset_game():
    for i in range(0, len(init_table_chess)):
        for j in range(0, len(init_table_chess)):
            init_table_chess[i][j] = ''

    for i in range(0, len(btn_list)):
        btn_list[i]['state'] = NORMAL
        btn_list[i]['image'] = img_bg

    start_player = random.randint(0, 1)
    if start_player == 0:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        init_table_chess[x][y] = 'X'
        btn_list[x * 3 + y].config(image=img_x)
    tk.mainloop()


def end_game():
    tk.destroy()


def btn_click_piece(buttons):
    for i in range(0, 3):
        for j in range(0, 3):
            if buttons['text'] == str(i*3+j+1):
                if init_table_chess[i][j] == "":
                    init_table_chess[i][j] = "O"
                    buttons.config(image=img_o)
                else:
                    return
    if buttons['text'] == "9":
        if init_table_chess[2][2] == "":
            init_table_chess[2][2] = "O"
            buttons.config(image=img_o)

    rs = check_game_over(init_table_chess)
    if rs == "X Win":
        disabled()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "X Win")
    if rs == "O Win":
        disabled()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "O Win")
    if equal_game():
        disabled()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Equal Game")
        return

    lbl_think.config(text='Machine is thinking...')
    tk.update_idletasks()
    x, y = handle_game(init_table_chess)
    init_table_chess[x][y] = "X"
    print(init_table_chess)
    for i in range(0, 3):
        for j in range(0, 3):
            if x == i and y == j:
                btn_list[i*3+j].config(image=img_x)

    rs = check_game_over(init_table_chess)
    if rs == "X Win":
        disabled()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "X Win")
    if rs == "O Win":
        disabled()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "O Win")
    if equal_game():
        disabled()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Equal Game")
        return
    lbl_think.config(text='You are thinking...')
    tk.update_idletasks()


def disabled():
    for i in range(0, len(btn_list)):
        btn_list[i].config(state=DISABLED)


def enabled():
    for i in range(0, len(btn_list)):
        btn_list[i].config(state=NORMAL)


def equal_game():
    flag = 0
    for i in range(0, len(init_table_chess)):
        for j in range(0, len(init_table_chess)):
            if init_table_chess[i][j] != '':
                flag += 1
    if flag == 9:
        return True
    return False


def init_board():
    text = 1
    canvas_board = Canvas(tk)
    canvas_board.pack()
    for i in range(3, 6):
        for j in range(0, 3):
            button = Button(canvas_board, text=str(text), state=NORMAL, image=img_bg, width=150, height=150)
            button.grid(row=i, column=j)
            btn_list.append(button)
            text += 1
    for i in range(0, len(btn_list)):
        btn_list[i]['command'] = lambda c=i: btn_click_piece(btn_list[c])


init_game()
tk.mainloop()