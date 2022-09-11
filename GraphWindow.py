from tkinter import messagebox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import plotly.express as px
import sys
import pathlib
import os
import time
from GraphSourse import GraphSourse 
#from ProgressBar import ProgressBar
import datetime
import pandas

import pdb
class GraphWindow(QWidget):
    def __init__(self, parent=None):
        super(GraphWindow, self).__init__(parent)
        self.gs = GraphSourse()
        self.w = QDialog(parent)
        self.db_path = os.path.join(os.path.dirname(sys.argv[0]),"DB\\")
        self.outputPath = os.path.join(os.path.dirname(sys.argv[0]),"output\\")
        self.initUI() # UIの初期化

    def initUI(self): # UIの初期化をするメソッド
        self.w.resize(400, 300) # ウィンドウの大きさの設定(横幅, 縦幅)
        self.w.move(400, 300) # ウィンドウを表示する場所の設定(横, 縦)
        self.w.setWindowTitle('PyQt5 sample GUI') # ウィンドウのタイトルの設定

        self.dbPathBtn = QPushButton('DB Directory', self) # ボタンウィジェット作成
        self.dbPathBtn.clicked.connect(self.getDbPathDialog)
        self.dbPathTxt = QLineEdit(self)
        self.dbPathTxt.setText(self.db_path)
        self.dbinfolbl = QLabel(self)
        self.dbinfolbl.setText("DB Path")

        self.dbpathlbl = QLabel(self)
        self.dbpathlbl.setText(self.db_path)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        self.dblbl = QLabel(self)
        self.dblbl.setText("DB Name")
        self.dbcb = QComboBox()
        self.dbcb.setEditable(True)
        self.dbcb.activated.connect(self.getDbTableData)
        self.dbbtn = QPushButton('取得', self) 
        self.dbbtn.clicked.connect(self.getDbName)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        self.tablelbl = QLabel(self)
        self.tablelbl.setText("Table Name")
        self.tablecb = QComboBox()
        self.tablecb.setEditable(True)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        self.selectYLbl = QLabel(self)
        self.selectYLbl.setText("縦軸")
        self.selectYCb = QComboBox()
#        self.selectYCb.setEditable(True)
#        self.selectYCb.activated.connect(self.getTateLabel)

        self.selectXLbl1 = QLabel(self)
        self.selectXLbl1.setText("横軸1")
        self.selectXCb1 = QComboBox()
#        self.selectXCb1.setEditable(True)
#        self.selectXCb1.activated.connect(self.getYoko1Label)

        self.selectXLbl2 = QLabel(self)
        self.selectXLbl2.setText("横軸2")
        self.selectXCb2 = QComboBox()
#        self.selectXCb2.setEditable(True)
#        self.selectXCb2.activated.connect(self.getYoko2Label)  

        self.selectXLbl3 = QLabel(self)
        self.selectXLbl3.setText("横軸3")
        self.selectXCb3 = QComboBox()
#        self.selectXCb3.setEditable(True)
#        self.selectXCb3.activated.connect(self.getYoko3Label)  

        self.selectXLbl4 = QLabel(self)
        self.selectXLbl4.setText("横軸4")
        self.selectXCb4 = QComboBox()
#        self.selectXCb4.setEditable(True)
#        self.selectXCb4.activated.connect(self.getYoko4Label)  

        self.selectXLbl5 = QLabel(self)
        self.selectXLbl5.setText("横軸5")
        self.selectXCb5 = QComboBox()
#        self.selectXCb5.setEditable(True)
#        self.selectXCb5.activated.connect(self.getYoko5Label)  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        self.graphTateLbl = QLabel(self)
        self.graphTateLbl.setText("縦軸名")
        self.graphTateName = QLineEdit()
        self.graphTateName.setText("寸法値[um]")

        self.graphTateMinLbl = QLabel(self)
        self.graphTateMinLbl.setText("Min")
        self.graphTateMin = QLineEdit()
        self.graphTateMin.setText("-999")

        self.graphTateMaxLbl = QLabel(self)
        self.graphTateMaxLbl.setText("Max")
        self.graphTateMax = QLineEdit()
        self.graphTateMax.setText("1")     

        self.graphYokoLbl = QLabel(self)
        self.graphYokoLbl.setText("横軸名")
        self.graphYokoName = QLineEdit()
        self.graphYokoName.setText("日付")
        
        self.graphYokoMinLbl = QLabel(self)
        self.graphYokoMinLbl.setText("Min")
        self.graphYokoMin = QLineEdit()
        self.graphYokoMin.setText("2000,1,1,0,0")

        self.graphYokoMaxLbl = QLabel(self)
        self.graphYokoMaxLbl.setText("Max")
        self.graphYokoMax = QLineEdit()
        self.graphYokoMax.setText("2030,1,1,0,0")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        self.graphTitleLbl = QLabel(self)
        self.graphTitleLbl.setText("グラフタイトル")
        self.graphTitle = QLineEdit()
        self.graphTitle.setText("title")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        self.runbtn = QPushButton('実行', self) 
        self.runbtn.clicked.connect(self.getDbData)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#        self.pbar = QProgressBar(self)
#        self.pbar.setGeometry(30, 40, 200, 25)
#        self.setWindowTitle('QProgressBar')

#        self.timer = QTimer()

        self.csvtxt = QLineEdit(self)
        self.csvbtn = QPushButton('CSV File', self) # ボタンウィジェット作成
        self.csvbtn.clicked.connect(self.getCsvTxtDialog)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         
        layout1_1 = QHBoxLayout()
        layout1_1.addWidget(self.dbPathBtn)
        layout1_1.addWidget(self.dbPathTxt)
        layout1_2 = QHBoxLayout()
        layout1_2.addWidget(self.dblbl)
        layout1_2.addWidget(self.dbcb)
        layout1_2.addWidget(self.dbbtn) 
        layout1_3 = QHBoxLayout()
        layout1_3.addWidget(self.tablelbl)
        layout1_3.addWidget(self.tablecb)
        layout1 = QVBoxLayout()
        layout1.addLayout(layout1_1)
        layout1.addLayout(layout1_2)
        layout1.addLayout(layout1_3)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        layout2_1 = QHBoxLayout()
        layout2_1.addWidget(self.selectYLbl)
        layout2_1.addWidget(self.selectYCb)
        layout2_2 = QHBoxLayout()
        layout2_2.addWidget(self.selectXLbl1)
        layout2_2.addWidget(self.selectXCb1)
        layout2_3 = QHBoxLayout()
        layout2_3.addWidget(self.selectXLbl2)
        layout2_3.addWidget(self.selectXCb2)
        layout2_4 = QHBoxLayout()
        layout2_4.addWidget(self.selectXLbl3)
        layout2_4.addWidget(self.selectXCb3)
        layout2_5 = QHBoxLayout()
        layout2_5.addWidget(self.selectXLbl4)
        layout2_5.addWidget(self.selectXCb4)
        layout2_6 = QHBoxLayout()
        layout2_6.addWidget(self.selectXLbl5)
        layout2_6.addWidget(self.selectXCb5)        
        layout2 = QVBoxLayout()
        layout2.addLayout(layout2_1)
        layout2.addLayout(layout2_2)
        layout2.addLayout(layout2_3)
        layout2.addLayout(layout2_4)
        layout2.addLayout(layout2_5)
        layout2.addLayout(layout2_6)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        layout3_1 = QHBoxLayout()
        layout3_1.addWidget(self.graphTateLbl)
        layout3_1.addWidget(self.graphTateName)
        layout3_2 = QHBoxLayout()
        layout3_2.addWidget(self.graphTateMinLbl)
        layout3_2.addWidget(self.graphTateMin)
        layout3_3 = QHBoxLayout()
        layout3_3.addWidget(self.graphTateMaxLbl)
        layout3_3.addWidget(self.graphTateMax)
        layout3_4 = QHBoxLayout()
        layout3_4.addWidget(self.graphYokoLbl)
        layout3_4.addWidget(self.graphYokoName)
        layout3_5 = QHBoxLayout()
        layout3_5.addWidget(self.graphYokoMinLbl)
        layout3_5.addWidget(self.graphYokoMin)
        layout3_6 = QHBoxLayout()
        layout3_6.addWidget(self.graphYokoMaxLbl)
        layout3_6.addWidget(self.graphYokoMax)        
        layout3 = QVBoxLayout()
        layout3.addLayout(layout3_1)
        layout3.addLayout(layout3_2)
        layout3.addLayout(layout3_3)
        layout3.addLayout(layout3_4)
        layout3.addLayout(layout3_5)
        layout3.addLayout(layout3_6)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        layout4_1 = QHBoxLayout()
        layout4_1.addWidget(self.graphTitleLbl)
        layout4_1.addWidget(self.graphTitle)
        layout4 = QVBoxLayout()
        layout4.addLayout(layout4_1)     
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        layout10 = QHBoxLayout()
        layout10.addWidget(self.runbtn)

        layout = QVBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)
        layout.addLayout(layout10)
        self.w.setLayout(layout)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def getDbTableData(self):
        self.tablecb.clear()
        self.gs.setDbdata(self.dbpathlbl.text() + self.dbcb.currentText())
        self.tablecb.addItems(self.gs.db_tablelist)
        if self.gs.db_tablelist:
            self.gs.getAxisList(self.tablecb.currentText())
            self.selectYCb.clear()
            self.selectYCb.addItems(self.gs.dbAxisList)
            self.selectXCb1.clear()
            self.selectXCb1.addItems(self.gs.dbAxisList)
            self.selectXCb2.clear()
            self.selectXCb2.addItems(self.gs.dbAxisList)        
            self.selectXCb3.clear()
            self.selectXCb3.addItems(self.gs.dbAxisList)
            self.selectXCb4.clear()
            self.selectXCb4.addItems(self.gs.dbAxisList)
            self.selectXCb5.clear()
            self.selectXCb5.addItems(self.gs.dbAxisList)

    def getDbTxtDialog(self):
        filePath = QFileDialog.getOpenFileName(
        QFileDialog(), caption="", directory="", filter="*.*")[0] 
        if filePath:
            self.dbtxt.setText(filePath)

    def getCsvTxtDialog(self):
        filePath = QFileDialog.getOpenFileName(
        QFileDialog(), caption="", directory="", filter="*.*")[0] 
        if filePath:
            self.csvtxt.setText(filePath)

    def show(self):
        self.w.exec_()



    def getDbName(self):
        db_folder = pathlib.Path(self.db_path)
        db_dirs = [x.name for x in db_folder.iterdir() if x.suffix==".db"]
        self.dbcb.clear()
        self.tablecb.clear()
        self.dbcb.addItems(db_dirs)
        if db_dirs:
            self.getDbTableData()
        else:
            QMessageBox.critical(None, "My message", "ファイルがありません。", QMessageBox.Ok)

    def getDbData(self):
#        time.sleep(1)
#        pbarWindow = ProgressBar()
#        pbarWindow.show()

        yList = []
        if self.selectXCb1.currentText():
            yList.append(self.selectXCb1.currentText())
        if self.selectXCb2.currentText():
            yList.append(self.selectXCb2.currentText())
        if self.selectXCb3.currentText():
            yList.append(self.selectXCb3.currentText())
        if self.selectXCb4.currentText():
            yList.append(self.selectXCb4.currentText())
        if self.selectXCb5.currentText():
            yList.append(self.selectXCb5.currentText())

        df = self.gs.db.query("select * from " +self.tablecb.currentText() + ";")
        xlabel = self.selectYCb.currentText()
        ylabel = yList
        ##time filter

        
        minTime = self.graphYokoMin.text().split(",")
        maxTime = self.graphYokoMax.text().split(",")
        dt1 = datetime.datetime(int(minTime[0]),int(minTime[1]),int(minTime[2]),int(minTime[3]),int(minTime[4]))
        dt2 = datetime.datetime(int(maxTime[0]),int(maxTime[1]),int(maxTime[2]),int(maxTime[3]),int(maxTime[4]))
        minfil =[1.1,1,1]
        maxfil =[3,3,3]

        df[xlabel] = pandas.to_datetime(df[xlabel])
        if dt1:
            df = df[df[xlabel] >= dt1]
        if dt2:
            df = df[df[xlabel] <= dt2]

        ##Number filter
        minThreash = float(self.graphTateMin.text())
        maxThreash = float(self.graphTateMax.text())
 
        for i, l in enumerate(ylabel):
            df.loc[df[l] < minThreash, l] = None
            df.loc[df[l] > maxThreash, l] = None

        fig = px.line(df,x=df[xlabel].values,y=yList, render_mode='webgl')
        fig.update_xaxes(title=self.graphYokoName.text()) 
        fig.update_yaxes(title=self.graphTateName.text())
        ###fig.update_xaxes(range=(1,3)) # X軸の最大最小値を指定
        fig.update_layout(title=self.graphTitle.text()) # グラフタイトルを設定

        fig.update_layout(font={"family":"Meiryo", "size":20}) # フォントファミリとフォントサイズを指定
        fig.update_xaxes(rangeslider={"visible":True}) # X軸に range slider を表示（下図参照）
        fig.update_layout(showlegend=True) # 凡例を強制的に表示（デフォルトでは複数系列あると表示）
        fig.update_layout(template="plotly_white") # 白背景のテーマに変更

        fig.write_html(self.outputPath + 'hoge.html') 
        QMessageBox.critical(None, "My message", "完了", QMessageBox.Ok)
#        fig.show()

    # 時間のイベントハンドラ
    def timerEvent(self, e):

        # プログレスバーが100%以上になったらタイマーを止め、ボタンラベルをFinishedにする
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        # 1%ずつ数字を増やしていく
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def getDbPathDialog(self):
        rootpath = os.path.abspath(os.path.dirname("__file__"))
        filePath = QFileDialog.getExistingDirectory(None, "rootpath", rootpath)
        self.db_path = filePath
        self.dbPathTxt.setText(filePath)
