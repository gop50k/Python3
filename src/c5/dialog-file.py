# coding: UTF-8
# htmlのPathを表示するプログラム

import tkinter.filedialog as fd
path = fd.askopenfilename(
    title = '処理ファイルを選択してください',
    filetypes = [('HTML', '.html')]
)

print(path)
