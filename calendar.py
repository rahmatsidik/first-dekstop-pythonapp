from PyQt5 import QtCore, QtWidgets

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Reminder")
    cal = QtWidgets.QCalendarWidget(gridVisible=True)
    lay = QtWidgets.QVBoxLayout(window)
    lay.addWidget(cal)

    @QtCore.pyqtSlot(QtCore.QDate)
    def get_date(date): # <--- date parameter
        print(str(date))

    cal.clicked.connect(get_date)
    window.show()
    sys.exit(app.exec())