import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src import process


class CInputDialogWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQtInputDialog 예제")
        self.setGeometry(100, 100, 200, 250)

        self.label = QLabel("Wafer : ", self)
        self.label.move(20, 20)
        self.label.resize(150, 20)

        self.label2 = QLabel("Column : ", self)
        self.label2.move(20, 20)
        self.label2.resize(150, 80)

        self.waferEdit = QLineEdit("All", self)
        self.waferEdit.move(80, 20)
        self.waferEdit.resize(100, 20)

        self.columnEdit = QLineEdit("All", self)
        self.columnEdit.move(80, 50)
        self.columnEdit.resize(100, 20)

        self.saveEdit = QCheckBox("Save", self)
        self.saveEdit.move(30, 80)
        self.saveEdit.toggle()

        self.showEdit = QCheckBox("Show", self)
        self.showEdit.move(30, 100)
        self.showEdit.toggle()

        self.btnSave = QPushButton("OK", self)
        self.btnSave.move(50, 200)
        self.btnSave.clicked.connect(self.btnInput_clicked)


    def btnInput_clicked(self):
        wafer = self.waferEdit.text()
        column = self.columnEdit.text()
        save = self.saveEdit.isChecked()
        show = self.showEdit.isChecked()
        try:
            if wafer == '' or column == '':
                raise ValueError('There is blank')
            if wafer == 'All' and column == 'All':
                process.all(save, show)
            elif wafer != 'All' and column == 'All':
                process.wafer(wafer, save, show)
            else:
                process.coordinate(wafer, column, save, show)
        except ValueError as e:
            print('Error: ', e, ', Pleas Input Again')
        #QCoreApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CInputDialogWindow()
    window.show()
    app.exec_()