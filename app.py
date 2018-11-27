import paramiko
import sys

from PyQt5 import QtWidgets

import config.config as config

from searcher_ui import Ui_Searcher


class MainWindow(Ui_Searcher):

    def __init__(self, dialog):
        Ui_Searcher.__init__(self)
        self.setupUi(dialog)

        self.SearchButton.clicked.connect(self.search)
        self.ExitButton.clicked.connect(self.close_app)

    def search(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(config.SERVER_CONFIG['host'], username=config.SERVER_CONFIG['username'], key_filename=config.SERVER_CONFIG['key_filename'])
        stdin, stdout, stderr = ssh.exec_command('pwd')
        print(stdout.readlines())

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
