import re, string

class SearchUtility:

    def find_pattern(selfs, instance_handler, msg):

        nonprintable = re.compile(b'[^%s]+' % re.escape(string.printable.encode('ascii')))

        folderList = instance_handler.listdir('/ORACLE/appl/fs1/EBSapps/appl/')
        folderList.sort()
        try:
            for d in folderList:
                print("Befor " + d)
                try:
                    fileList = instance_handler.listdir("/ORACLE/appl/fs1/EBSapps/appl/" + str(d) + "/12.0.0/reports/PL/")
                    for f in fileList:
                        if re.match('^(XX)|(XC)', f):
                            isValid = False
                            report_lines = ""
                            print('File name: ' + f)
                            with instance_handler.open('/ORACLE/appl/fs1/EBSapps/appl/' + str(d) + '/12.0.0/reports/PL/' + str(f), "rb") as testFile:
                                for line in nonprintable.split(testFile.read()):
                                    line = line.decode('UTF-8')
                                    if (line.lower().find('FND FLEXIDVAL'.lower()) != -1):
                                        # report_lines += line
                                        #isValid = True

                                    #if isValid:
                                        # print(f)
                                        print('Find line: ' + line)
                                        msg.setPlaceholderText(line)

                except Exception as e:
                    print(d)
                    print(e)

        except Exception as e:
            print(e)
