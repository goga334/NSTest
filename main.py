import sys 
import os
from PyQt6 import QtWidgets
import design
import sqlite3 

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)  
        self.chooseFile.clicked.connect(self.browse_folder)
        self.pushButton_2.clicked.connect(self.import_library)
        self.pushButton_3.clicked.connect(self.append_library)  
        self.lineEdit_2.textChanged.connect(self.find_words)
        self.addWord.clicked.connect(self.add_word)

    def import_library(self):
        try:
            print(self.label_5.text())
            word_to_add = open(self.label_5.text())
            cur.execute(f"DELETE FROM words;")
            for i in word_to_add:
                cur.execute(f"INSERT INTO words VALUES('{i[:-1]}');")
                conn.commit()
        except:
            print("Could not open the library")


    def append_library(self):
        try:
            print(self.label_5.text())
            word_to_add = open(self.label_5.text())
            for i in word_to_add:
                cur.execute(f"INSERT INTO words VALUES('{i[:-1]}');")
                conn.commit()
        except:
            print("Could not open the library")

    def find_words(self):
        search = self.lineEdit_2.text()
        cur.execute(f"SELECT * FROM words WHERE word LIKE '%{search}%';")
        result = cur.fetchall()
        self.listWidget.clear()
        for word_found in result:
            self.listWidget.addItem(word_found[0])
            if self.listWidget.count() > 9:
                break

    def add_word(self):
        word_to_add = self.lineEdit.text()
        cur.execute(f"INSERT INTO words VALUES('{word_to_add}');")
        conn.commit()

    def browse_folder(self):
        self.listWidget.clear() 
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Choose file")

        if file:
            self.label_5.setText(file[0])

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp() 
    window.show() 
    
    cur.execute(f"CREATE TABLE IF NOT EXISTS words(word TEXT);")
    conn.commit()
    app.exec()

if __name__ == '__main__': 
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    main()  