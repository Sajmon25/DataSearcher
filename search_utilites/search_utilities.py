import re

class SearchUtility:

    def find_pattern(selfs, instance_handler, msg):

        folderList = instance_handler.listdir('/ORACLE/appl/fs1/EBSapps/appl/')
        folderList.sort()
        try:
            for d in folderList:
                try:
                    fileList = instance_handler.listdir("/ORACLE/appl/fs1/EBSapps/appl/" + str(d) + "/12.0.0/reports/PL/")
                    for f in fileList:
                        if re.match('^(XX)|(XC)', f):
                            isValid = False
                            report_lines = ""
                            with instance_handler.open('/ORACLE/appl/fs1/EBSapps/appl/' + str(d) + '/12.0.0/reports/PL/' + str(f), 'r') as testFile:
                                for line in testFile:
                                    if (line.decode("utf-8").lower().find('attribute_category'.lower()) != -1):
                                        report_lines += line
                                        isValid = True

                                    if isValid:
                                        print(f)
                                        print(report_lines)
                                        msg.setPlaceholderText(report_lines)

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)
