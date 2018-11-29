import sys
import search_utilites.search_utilities as su
from PyQt5 import QtWidgets
from searcher_ui import Ui_Searcher
from Connection import Connection

class MainWindow(Ui_Searcher):

    def __init__(self, dialog):
        Ui_Searcher.__init__(self)
        self.setupUi(dialog)

        self.SearchButton.clicked.connect(self.search)
        self.ExitButton.clicked.connect(self.close_app)

    def search(self):

        # connect to server
        self.msg.appendPlainText('Connect to server...')
        conn = Connection()
        ftp = conn.get_ftp_connection()
        # get file path list
        self.msg.appendPlainText('Create files list...')

        file_path_list = su.SearchUtility.get_filepath_list(self, ftp)
        # analise files step by step and return output
        for file_path in file_path_list:
            self.msg.appendPlainText("Analise file: "+file_path)
            self.msg.appendPlainText(su.SearchUtility.extract_str_from_bin(self, ftp, file_path, 'TRX_NUMBER'))

    @staticmethod
    def close_app():
        print('Exit...')




if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()

	prog = MainWindow(dialog)

	dialog.show()
	sys.exit(app.exec_())
