import sys
from MainWidget import MainWidget
from PyQt5 import QtWidgets

def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

def main():
	sys._excepthook = sys.excepthook
	sys.excepthook = exception_hook
	app = QtWidgets.QApplication(sys.argv)
	widget = MainWidget()
	widget.show()
	try:
		app.exec_()
	except:
		print('exiting')
if __name__ == '__main__':
	main()