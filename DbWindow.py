from PyQt5.QtWidgets import *
import os
import pandas
import sqlite3
import pathlib

class DbWindow(QWidget):
    def __init__(self, parent=None):
        super(DbWindow, self).__init__(parent)
        self.w = QDialog(parent)
        self.initUI() # UIの初期化
    def initUI(self): # UIの初期化をするメソッド
        self.w.resize(400, 300) # ウィンドウの大きさの設定(横幅, 縦幅)
        self.w.move(400, 300) # ウィンドウを表示する場所の設定(横, 縦)
        self.w.setWindowTitle('PyQt5 sample GUI') # ウィンドウのタイトルの設定
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        self.csvbtn = QPushButton('FilePath(.csv)', self) # ボタンウィジェット作成
        self.csvbtn.clicked.connect(self.getCsvTxtDialog)
        self.csvtxt = QLineEdit(self)

        self.wi = QListWidget()
        
        self.srchbtn = QPushButton('先頭行取得', self) 
        self.srchbtn.clicked.connect(self.getIndex)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        self.dblbl = QLabel(self)
        self.dblbl.setText("DB Name")
        self.dbtxt = QLineEdit(self)
        self.dbtxt.setText("graph")

        self.tbllbl = QLabel(self)
        self.tbllbl.setText("TABLE Name")
        self.tbltxt = QLineEdit(self)
        self.tbltxt.setText("phv")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        self.wi2 = QLineEdit()
        self.wi2.setMaxLength(1000)
        self.wi2.setPlaceholderText("Enter your text ex) 1,2,3,4")

        self.makeDBbtn = QPushButton('DB作成', self) 
        self.makeDBbtn.clicked.connect(self.makeDbFile)

 
        layout1 = QHBoxLayout()
        layout1.addWidget(self.csvbtn)
        layout1.addWidget(self.csvtxt)
        layout1.addWidget(self.srchbtn)
        
        layout2 = QHBoxLayout()
        layout2.addWidget(self.dblbl)
        layout2.addWidget(self.dbtxt)
        layout2.addWidget(self.tbllbl)
        layout2.addWidget(self.tbltxt)

        layout3 = QHBoxLayout()
        layout3.addWidget(self.wi)

        layout4 = QHBoxLayout()
        layout4.addWidget(self.wi2)

        layout5 = QHBoxLayout()
        layout5.addWidget(self.makeDBbtn)

        layout = QVBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)
        layout.addLayout(layout5)



        self.w.setLayout(layout)

    def getIndex(self):
        if os.path.isfile(self.csvtxt.text()):
            if self.csvtxt.text().endswith('.csv'):
                with open(self.csvtxt.text(), 'r') as f:
                    index = f.readlines()[0]
                index = index.replace("\n","").split("\t")
                self.wi.clear()
                self.wi.addItems(index)

                self.csv_category = index
                print("index",index)
            else:
                QMessageBox.critical(None, "My message", "csvファイルを指定してください。", QMessageBox.Ok)
        else:
            QMessageBox.critical(None, "My message", "ファイルがありません。", QMessageBox.Ok)

    def getDbTxtDialog(self):
        filePath = QFileDialog.getOpenFileName(
        QFileDialog(), caption="", directory="", filter="*.db")[0] 
        if filePath:
            self.dbtxt.setText(filePath)

    def getCsvTxtDialog(self):
        filePath = QFileDialog.getOpenFileName(
        QFileDialog(), caption="", directory="", filter="*.csv")[0] 
        if filePath:
            self.csvtxt.setText(filePath)

    def show(self):
        self.w.exec_()

    def makeDbFile(self):
        db_folder = os.path.join(os.path.dirname(__file__),"DB")
        pathlib.Path(db_folder).mkdir(exist_ok=True)
        db_file = db_folder +"/" + self.dbtxt.text()+".db"
        ylabel = self.wi2.text().split(",")
        conn = sqlite3.connect(db_file) # DBを作成する（既に作成されていたらこのDBに接続する）
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS '+self.tbltxt.text()+'(id INTEGER PRIMARY KEY AUTOINCREMENT, t,TEXT,v1 REAL, v2 REAL, v3 REAL)')
        rdf = pandas.read_sql('SELECT * FROM '+self.tbltxt.text(), conn)
        df = pandas.read_table(self.csvtxt.text(),  header = None, names = ylabel)
        ccdf = pandas.concat([df, rdf], join='inner')
        ccdf.drop_duplicates()
        df.to_sql(self.tbltxt.text(), conn,if_exists='replace',index=False)
        conn.close()
        QMessageBox.information(None, "My message", "DB作成完了", QMessageBox.Ok)
        