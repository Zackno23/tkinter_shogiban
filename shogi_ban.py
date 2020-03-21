import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()

        self.geometry('{}x{}+{}+{}'.format(400, 400, 300, 100))
        self.resizable(width=0, height=0)

    def run(self):
        self.mainloop()

    def set_widgets(self):
        ### 将棋盤を作る ###
        self.board = tk.Canvas(self, width=400, height=400, bg="Peach Puff3")
        self.board.pack()
        self.title = ('shogi-ban')
        self.iconbitmap("shogi-icon.png")

        ### 長方形を作る ###
        # 将棋盤の情報
        # -1 -> 盤の外, 0 -> 空白
        self.board2info = [-1] * 11 + [[0, -1][i in [0, 10]] for i in range(11)] * 9 + [-1] * 11
        # {tag: position}
        self.tag2pos = {}
        # 座標からtagの変換
        self.z2tag = {}
        # 符号
        self.numstr = "123456789"
        self.kanstr = "一二三四五六七八九"
        for i, y in zip(self.kanstr, range(20, 380, 40)):
            for j, x in zip(self.numstr[::-1], range(20, 380, 40)):
                pos = (x, y, x + 40, y + 40)
                tag = j + i
                self.tag2pos[tag] = pos[:2]
                self.board.create_rectangle(*pos, fill="Peach puff3", tags=tag)
                self.z2tag[self.z_coordinate(tag)] = tag
        for turn, i in zip([0, 1], ["一", "九"]):
            for j in self.numstr[::-1]:
                tag = j + i
                self.draw_text(tag, turn)
                self.board2info[self.z_coordinate(tag)] = [1, 2][turn]
        self.get_board_info()
        # バインディングの設定


    def z_coordinate(self, tag):
        x, y = self.numstr[::-1].index(tag[0]) + 1, self.kanstr.index(tag[1]) + 1
        return y * 11 + x

    def get_board_info(self, a=None, b=None):
        tags = "" if a is None else "\n{} -> {}".format(a, b)
        board_format = " {:2d} " * 11
        print(board_format)

        print(tags, *[board_format.format(*self.board2info[i:i + 11]) \
                      for i in range(0, 121, 11)], sep='\n')
    def draw_text(self, tag, turn):
        x, y = self.tag2pos[tag]
        self.board.create_text(x+20, y+20,
                               font=("Helvetica", 10, "bold"),
                               angle=[180, 0][turn],
                               text=["歩", "歩"][turn],
                               tags=tag)

if __name__ == '__main__':
    app = App()

    app.set_widgets()
    app.run()
    print(app.board_format)
