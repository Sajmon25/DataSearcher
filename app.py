import sys
from Connection import Connection
from PyQt5 import QtWidgets
from searcher_ui import Ui_Searcher
import search_utilites.search_utilities as Su


class MainWindow(Ui_Searcher):

    def __init__(self, dialog):
        Ui_Searcher.__init__(self)
        self.setupUi(dialog)

        self.SearchButton.clicked.connect(self.search)
        self.ExitButton.clicked.connect(self.close_app)

    def search(self):

        # connect to server
        conn = Connection()
        ftp = conn.get_ftp_connection()
        # get file path list
        
        # analise files step by step and return output



        # stdin, stdout, stderr = ssh.exec_command('pwd')
        # int(stdout.readlines())
        search = Su.SearchUtility()
        search.find_pattern(ftp, self.msg)

        # hostname = "poligonap01.fideltronik.com.pl"  # example
        # response = os.system("ping " + hostname)
        #
        # # and then check the response...
        # if response == 0:
        #     print(hostname, 'is up!')
        # else:
        #     print(hostname, 'is down!')
        print("Searching..." + self.Pattern.text())

    @staticmethod
    def close_app():
        print('Exit...')




if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()

	prog = MainWindow(dialog)

	dialog.show()
	sys.exit(app.exec_())
