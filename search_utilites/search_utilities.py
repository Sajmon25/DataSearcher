import re
import string


class SearchUtility:

    def find_pattern(self, instance_handler, msg):

        nonprintable = re.compile(b'[^%s]+' % re.escape(string.printable.encode('ascii')))

        folder_list = instance_handler.listdir('/ORACLE/appl/fs1/EBSapps/appl/')
        folder_list.sort()
        try:
            for d in folder_list:
                print("Befor " + d)
                try:
                    file_list = instance_handler.listdir("/ORACLE/appl/fs1/EBSapps/appl/" + str(d) +
                                                         "/12.0.0/reports/PL/")
                    for f in file_list:
                        if re.match('^(XX)|(XC)', f):
                            print('File name: ' + f)
                            with instance_handler.open('/ORACLE/appl/fs1/EBSapps/appl/' + str(d) + '/12.0.0/reports/PL/'
                                                       + str(f), "rb") as testFile:
                                for line in nonprintable.split(testFile.read()):
                                    line = line.decode('UTF-8')
                                    if line.lower().find('FND FLEXIDVAL'.lower()) != -1:
                                        print('Find line: ' + line)
                                        msg.setPlaceholderText(line)

                except Exception as e:
                    print(d)
                    print(e)

        except Exception as e:
            print(e)

    def get_filepath_list(self, instance_handler):

        filepath_list = []

        modules_list = instance_handler.listdir('/ORACLE/appl/fs1/EBSapps/appl/')
        modules_list.sort()

        try:
            for module in modules_list:

                dir_path = "/ORACLE/appl/fs1/EBSapps/appl/" + str(module) + "/12.0.0/reports/PL/"
                try:
                    file_list = instance_handler.listdir(dir_path)
                    for file_name in file_list:
                        if re.match('^(XX)|(XC)', file_name):
                            filepath_list.append(dir_path + str(file_name))
                except Exception:
                    print(dir_path+" path doesn't exists.")

        except Exception as e:
            print(e)

        return filepath_list

    def extract_str_from_bin(self, ih, file_path, pattern):

        match_strings = ''
        nonprintable = re.compile(b'[^%s]+' % re.escape(string.printable.encode('ascii')))

        with ih.open(file_path, "rb") as testFile:
            for line in nonprintable.split(testFile.read()):
                line = line.decode('UTF-8')
                if line.lower().find(pattern.lower()) != -1:
                    match_strings += line+"\n"

        return match_strings