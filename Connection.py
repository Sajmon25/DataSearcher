import paramiko
import config.config as config


class Connection(object):

    ssh = ''

    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(config.SERVER_CONFIG['host'], username=config.SERVER_CONFIG['username'],
                         key_filename=config.SERVER_CONFIG['key_filename'])

    def __del__(self):
        self.ssh.close()

    def get_ftp_connection(self):
        return self.ssh.open_sftp()
