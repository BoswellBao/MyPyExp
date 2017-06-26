import os
import xlrd
from xlwt import easyxf
from xlutils.copy import copy

class WriteExcle():

    def __init__(self, file_path, sheet_name, caseName, flag, content):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.caseName = caseName
        self.flag = flag
        self.content = content

    def writeIn(self):
        try:
            rf = xlrd.open_workbook(self.file_path,formatting_info=True)#保持格式
            rf_sheet = rf.sheet_by_name(self.sheet_name)
            rownum = rf_sheet.nrows
            colnum = rf_sheet.ncols
            case_row_index = 0
            for i in range(rownum):
                if(self.caseName in rf_sheet.row_values(i)):
                    case_row_index = i
                    break

            wf = copy(rf)
            index = wf.sheet_index(self.sheet_name)
            wt_sheet = wf.get_sheet(index)

            wt_sheet.write(case_row_index,colnum - 2,self.flag)
            wt_sheet.write(case_row_index,colnum - 1,self.content)
            wf.save(self.file_path)
        except Exception as e:
            print(e)


