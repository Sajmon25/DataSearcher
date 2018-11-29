import paramiko
import sys

from PyQt5 import QtWidgets

import config.config as config
import search_utilites.search_utilities as Su
from searcher_ui import Ui_Searcher


class MainWindow(Ui_Searcher):

    def __init__(self, dialog):
        Ui_Searcher.__init__(self)
        self.setupUi(dialog)

        self.SearchButton.clicked.connect(self.search)
        self.ExitButton.clicked.connect(self.close_app)

    def search(self):

        # connect to server

        # get file path list

        # analise files step by step and return output
        

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(config.SERVER_CONFIG['host'], username=config.SERVER_CONFIG['username'], key_filename=config.SERVER_CONFIG['key_filename'])
        ftp = ssh.open_sftp()
        # stdin, stdout, stderr = ssh.exec_command('pwd')
        # int(stdout.readlines())

        Search = Su.SearchUtility()
        Search.find_pattern(ftp, self.msg)
        ssh.close()
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
