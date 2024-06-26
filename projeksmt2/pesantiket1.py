# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 551, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout_2.addWidget(self.tableWidget, 5, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 5, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 3, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton.clicked.connect(self.save_data) # type: ignore
        self.pushButton_4.clicked.connect(self.update_data) # type: ignore
        self.pushButton_3.clicked.connect(self.delete_data) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Initialize database
        self.init_db()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NAMA"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "KELAS"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PUKUL"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "TUJUAN"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "HARGA"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Semarang"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Jakarta"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Surabaya"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Madiun"))
        self.comboBox.setItemText(0, _translate("MainWindow", "VIP"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Bisnis"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Ekonomi"))
        self.label_4.setText(_translate("MainWindow", "PUKUL:"))
        self.label.setText(_translate("MainWindow", "PEMESANAN TIKET KERETA STASIUN BALAPAN"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "06.00"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "10.00"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "15.00"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "18.00"))
        self.label_2.setText(_translate("MainWindow", "NAMA:"))
        self.label_5.setText(_translate("MainWindow", "TUJUAN:"))
        self.label_3.setText(_translate("MainWindow", "KELAS:"))
        self.pushButton_4.setText(_translate("MainWindow", "Update"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))
        self.pushButton.setText(_translate("MainWindow", "OK"))

    def init_db(self):
        self.conn = sqlite3.connect('tickets.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                nama TEXT,
                kelas TEXT,
                pukul TEXT,
                tujuan TEXT,
                harga INTEGER
            )
        ''')
        self.conn.commit()

    def save_data(self):
        nama = self.lineEdit.text()
        kelas = self.comboBox.currentText()
        pukul = self.comboBox_2.currentText()
        tujuan = self.comboBox_3.currentText()

        if kelas == "VIP":
            harga = 500000
        elif kelas == "Bisnis":
            harga = 350000
        else:
            harga = 100000

        self.c.execute('''
            INSERT INTO tickets (nama, kelas, pukul, tujuan, harga) 
            VALUES (?, ?, ?, ?, ?)
        ''', (nama, kelas, pukul, tujuan, harga))
        self.conn.commit()
        self.load_data()

    def load_data(self):
        self.c.execute('SELECT * FROM tickets')
        rows = self.c.fetchall()
        self.tableWidget.setRowCount(0)
        for row in rows:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            for i in range(len(row)-1):
                self.tableWidget.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(row[i+1])))
            self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(row[5])))

    def update_data(self):
        selected = self.tableWidget.currentRow()
        if selected >= 0:
            nama = self.lineEdit.text()
            kelas = self.comboBox.currentText()
            pukul = self.comboBox_2.currentText()
            tujuan = self.comboBox_3.currentText()

            if kelas == "VIP":
                harga = 500000
            elif kelas == "Bisnis":
                harga = 350000
            else:
                harga = 100000

            self.c.execute('''
                UPDATE tickets 
                SET nama=?, kelas=?, pukul=?, tujuan=?, harga=?
                WHERE id=?
            ''', (nama, kelas, pukul, tujuan, harga, selected+1))
            self.conn.commit()
            self.load_data()

    def delete_data(self):
        selected = self.tableWidget.currentRow()
        if selected >= 0:
            self.c.execute('DELETE FROM tickets WHERE id=?', (selected+1,))
            self.conn.commit()
            self.load_data()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
