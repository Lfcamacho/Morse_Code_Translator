from PyQt5.QtWidgets import *
from gui_morsecode import *
from PyQt5.QtCore import pyqtSignal
import morse

# Thread class used to calculate all the possible results returned from morsedecoder() function without GUI freezing
# This class takes as input the morse code you want to translate and emits the list with all its answers to PrintAnswers method
# Run method starts when you call thread1.start()

class MyThread(QtCore.QThread):
    sig = pyqtSignal(list, str)

    def __init__(self, input_code):
        QtCore.QThread.__init__(self)
        self.input_code = input_code

    def run(self):
        try:   
            answer = morse.morsedecoder(self.input_code)
            self.sig.emit(answer, "")
        except:
            self.sig.emit([], "error")

# Main GUI class
class AppWindow(QMainWindow):
    sig = pyqtSignal(list, str)     

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        MainWindow = QtWidgets.QMainWindow()
        self.ui.setupUi(self)                   # Draw main widgets in GUI
        self.MainWindow = QMainWindow
        
        self.ui.input_code.setFocus()                               
        self.ui.translate_button.clicked.connect(self.clicked)      # start when translate button pressed
        self.ui.input_code.returnPressed.connect(self.clicked)      # start when click enter

        self.show()

    # Calculate all the answers 
    def clicked(self):
        self.ui.listWidget.clear()
        self.ui.statusbar.showMessage("Loading...")
        self.input_code = self.ui.input_code.text()
        self.thread1 = MyThread(self.input_code)
        self.thread1.sig.connect(self.PrintAnswers)
        self.thread1.start()                            # Start of Thread for morsedecoder

    # Show answers in QListWidget
    def PrintAnswers(self, answer, error):
        # If an error is detected
        if error == "error":        
            self.ui.statusbar.showMessage("This is not a valid input try using only . and -")
            self.msg = QtWidgets.QMessageBox()
            self.msg.setWindowTitle("Invalid Input")
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setText("Invalid input\nThis is not a valid input. Try using only . and -")
            self.msg.exec_()
        else:
            self.ui.statusbar.showMessage('Result: '+str(len(answer))+" options")
            self.ui.listWidget.addItems(answer)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())