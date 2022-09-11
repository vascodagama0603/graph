from PyQt5.QtWidgets import *
import datetime
import pathlib
import os

class SettingWindow():
    def __init__(self, parent=None):
        super(GraphWindow, self).__init__(parent)
        self.w = QDialog(parent)
        self.initUI() # UIの初期化

    def initUI(self): # UIの初期化をするメソッド
        self.w.resize(400, 300) # ウィンドウの大きさの設定(横幅, 縦幅)
        self.w.move(400, 300) # ウィンドウを表示する場所の設定(横, 縦)
        self.w.setWindowTitle('PyQt5 sample GUI') # ウィンドウのタイトルの設定

    def show(self):
        self.w.exec_()
