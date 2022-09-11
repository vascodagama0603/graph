import sys
import pdb

from DbWindow import DbWindow
from GraphWindow import GraphWindow
from SettingWindow import SettingWindow

from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # ボタンの作成
        GphPgbtn = QPushButton("&グラフ作成")
        GphPgbtn.clicked.connect(self.makeGraphW)

        DbPgbtn = QPushButton("&CSVからDB挿入")
        DbPgbtn.clicked.connect(self.makeDbW)

        Settingbtn = QPushButton("&設定")
        Settingbtn.clicked.connect(self.makeSettingW)

        layout = QHBoxLayout()
        layout.addWidget(DbPgbtn)
        layout.addWidget(GphPgbtn)
        self.setLayout(layout)

    def makeGraphW(self):
        graphWindow = GraphWindow()
        graphWindow.show()


    def makeDbW(self):
        dbWindow = DbWindow()
        dbWindow.show()

    def makeSettingW(self):
        settingWindow = SettingWindow()
        settingWindow.show() 
if __name__ == '__main__':
    app = QApplication(sys.argv) #PyQtで必ず呼び出す必要のあるオブジェクト
    main_window = MainWindow() #ウィンドウクラスのオブジェクト生成
    main_window.show() #ウィンドウの表示
    sys.exit(app.exec_()) #プログラム終了


