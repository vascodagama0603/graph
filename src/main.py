import sys

from view.DbWindow import DbWindow
from view.GraphWindow import GraphWindow
from view.TimeRenameWindow import TimeRenameWindow

from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # ボタンの作成
        GphPgbtn = QPushButton("&グラフ作成")
        GphPgbtn.clicked.connect(self.makeGraphW)

        Timebtn = QPushButton("&時間軸の設定")
        Timebtn.clicked.connect(self.makeTimeSettingW)

        DbPgbtn = QPushButton("&CSVからDB挿入")
        DbPgbtn.clicked.connect(self.makeDbW)


        layout = QHBoxLayout()
        layout.addWidget(DbPgbtn)
        layout.addWidget(Timebtn)
        layout.addWidget(GphPgbtn)
        self.setLayout(layout)

    def makeGraphW(self):
        graphWindow = GraphWindow()
        graphWindow.show()
        
    def makeDbW(self):
        dbWindow = DbWindow()
        dbWindow.show()

    def makeTimeSettingW(self):
        TimesettingWindow = TimeRenameWindow()
        TimesettingWindow.show() 
if __name__ == '__main__':
    app = QApplication(sys.argv) #PyQtで必ず呼び出す必要のあるオブジェクト
    main_window = MainWindow() #ウィンドウクラスのオブジェクト生成
    main_window.show() #ウィンドウの表示
    sys.exit(app.exec_()) #プログラム終了


